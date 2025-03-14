from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import CompanyModel
from schemas import CompanySchema, CompanyUpdateSchema

blp = Blueprint("Company", __name__, description="Operations on companies")


@blp.route("/company/<int:company_id>")
class Company(MethodView):
    @blp.response(200, CompanySchema)
    def get(self, company_id):
        company = CompanyModel.query.get_or_404(company_id)
        return company

    @blp.arguments(CompanyUpdateSchema)
    @blp.response(200, CompanySchema)
    def put(self, company_data, company_id):
        # https://bing.teclado.com/python-dictionary-merge-update-operators
        company = CompanyModel.query.get(company_id)

        if company:
            company.company_name = company_data["company_name"]
            company.workday_url = company_data["workday_url"]
            company.company_name = company_data["equity_ticker"]
    
        else:
            company = CompanyModel(id=company_id, **company_data)

        db.session.add(company)
        db.session.commit()

        return company

    def delete(self, company_id):
        # jwt = get_jwt()
        # is_admin = jwt.get("is_admin")
        # if not jwt.get("is_admin"):
        #     abort(401, message=is_admin)

        company = CompanyModel.query.get_or_404(company_id)
        db.session.delete(company)
        db.session.commit()
        return {"message": "company deleted."}


@blp.route("/companies")
class CompanyList(MethodView):
    @blp.response(200, CompanySchema(many=True))
    def get(self):
        return CompanyModel.query.all()

    @jwt_required()
    @blp.arguments(CompanySchema)
    @blp.response(201, CompanySchema)
    def post(self, company_data):
        company = CompanyModel(**company_data)

        try:
            db.session.add(company)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An Error occured")

        return company

from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class TagSchema(PlainTagSchema):
    store_id = fields.Int(load_only=True)
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)  ##, load_only=True)

class CompanySchema(Schema):
    id = fields.Int(dump_only=True)
    company_name = fields.Str(required=True)
    workday_url = fields.Url(required=True)
    equity_ticker = fields.Str(required=False,nullable=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class CompanyUpdateSchema(Schema):
    company_name = fields.Str()
    workday_url = fields.Url()
    equity_ticker = fields.Str()

class OpeningSchema(Schema):
    id = fields.Int(dump_only=True)
    company_id = fields.Int(required=True)
    total = fields.Int(required=False)
    new_york = fields.Int(required=False)

class ApplicationSchema(Schema):
    id = fields.Int(dump_only=True)
    company_id = fields.Int(required=True)
    job_title = fields.Str(required=True)
    job_req = fields.Str(required=False)
    status = fields.Str(required=False)
    date_submitted = fields.Date(required=False)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
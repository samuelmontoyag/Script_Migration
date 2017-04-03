from sqlalchemy import *

db = create_engine('sqlite:///app.db')

db.echo = False  # Try changing this to True and see what happens
metadata = BoundMetaData(db)

ventas = Table('ventas', metadata,
    Column('id', Integer, primary_key=True),
    Column('uuid', String(64)),
    Column('photo_type', String(64)),
    Column('amount', Float),
    Column('check_code', String(256)),
    Column('date', DateTime),
    Column('upload_date', DateTime),
)

ingreso = Table('ingresos', metadata,
    Column('id', Integer, primary_key=True),
    Column('uuid', String(64)),
    Column('pay_type', String(64)),
    Column('amount', Float),
    Column('date', DateTime),
    Column('id_venta', Integer),
)

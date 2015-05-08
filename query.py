# Note: this file will not run. It is only for recording answers.

# Part 2: Write queries

# Get the brand with the **id** of 8.

Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

Model.query.filter_by(name="Corvette", brand_name="Chevrolet").all()

# Get all models that are older than 1960.

Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.

Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands that are either discontinued or founded before 1950.

Brand.query.filter(db.or_(Brand.discontinued.isnot(None), Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name.isnot("Chevrolet")).first()

# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    """Given a string, return a list of brands (as objects) whose name contains
    or is equal to the input string."""

    brands = Brand.query.filter(Brand.name.like('%'+mystr+'%')).all()
    return brands


def get_models_between(start_year, end_year):
    """Given a start year and end year (two integers), return a list of 
    models (as objects) with years that fall between the start year and end year."""

    models = Model.query.filter(Model.year > start_year, Model.year < end_year).all()
    return models


# Part 3: Discussion Questions

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# This returns a query object, which is an instance of the BaseQuery class.

# 2. In your own words, what is an association table, and what *type* of relationship 
# does an association table manage?

# An association table is used to connect information in two other tables, while 
# not holding any additional data of its own; it doesn't correspond to an actual entity.
# It's used to manage a many-to-many relationship between the other two tables.


"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *
from collections import defaultdict

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
# brand = Brand.query.filter_by(id=8).one()

# # Get all models with the **name** Corvette and the **brand_name** Chevrolet.
# models = Model.query.filter_by(name="Corvette", brand_name="Chevrolet").all()

# # Get all models that are older than 1960.
# models = Model.query.filter(Model.year < 1960).all()

# # Get all brands that were founded after 1920.
# models = Model.query.filter(Model.year > 1920).all()

# # Get all models with names that begin with "Cor".
# models = Model.query.filter(Model.name.like("Cor%")).all()

# # Get all brands that were founded in 1903 and that are not yet discontinued.
# brands = Brand.query.filter(Brand.founded==1903, Brand.discontinued==None).all()

# # Get all brands that are either 1) discontinued (at any time) or 2) founded 
# # before 1950.
# brands = Brand.query.filter((Brand.founded<1950) | (Brand.discontinued.isnot(None))).all()

# # Get any model whose brand_name is not Chevrolet.
# brands = Brand.query.filter(Brand.name.isnot("Chevrolet")).all()

# Fill in the following functions. (See directions for more info.)
def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    cars = Model.query.filter_by(year=year).all()
    info = []

    for car in cars:
        info.append(" *** Model name: %s, Brand name: %s, HQ: %s *** "  % (car.name,
                                                          car.brand.name,
                                                          car.brand.headquarters))
    print info  

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    models = Model.query.all()
    car_dict = defaultdict(set)

    for model in models:
        car_dict[model.brand_name].add(model.name)

    for item in car_dict:
        car_models = []
        for values in car_dict[item]:
            car_models.append(values)
        print "Brand: %s    Model: %s" % (item, car_models)





# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
    # Value is [<B.Id=1 B.name=Ford Founded=1903 HQ=Dearborn, MI Discontinued=None>], 
    # which is whatever we specified it to return in the model.py file.
    # Datatype is a list of 1 object

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
    # An association table is a "fake" table. It doesn't have any real purpose outside
    # of conecting tables with no commonalites. Take our ratings project for an example,
    # if there were an additional genres table, we'd have to connect the movies table 
    # and the genres tables with an association table where each row containes 1 movie 
    # and 1 genre.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(thing):
    brands = Brand.query.filter(Brand.name.like('%{}%'.format(thing))).all()

    print brands

def get_models_between(start_year, end_year):
    brands = Brand.query.filter(Brand.founded>start_year, Brand.founded<end_year).all()

    list_models = []
    for brand in brands:
        model = Model.query.filter_by(brand_name=brand.name).all()
        for ea_model in model:
            list_models.append(ea_model)
    print list_models

""" Example pylib functions"""


def combined(resource, doc, env, *args, **kwargs):
    """ An example row generator function.

    Reference this function in a Metatab file as the value of a Datafile:

            Datafile: python:pylib#row_generator

    The function must yield rows, with the first being headers, and subsequenct rows being data.

    :param resource: The Datafile term being processed
    :param doc: The Metatab document that contains the term being processed
    :param args: Positional arguments passed to the generator
    :param kwargs: Keyword arguments passed to the generator
    :return:


    The env argument is a dict with these environmental keys:

    * CACHE_DIR
    * RESOURCE_NAME
    * RESOLVED_URL
    * WORKING_DIR
    * METATAB_DOC
    * METATAB_WORKING_DIR
    * METATAB_PACKAGE

    It also contains key/value pairs for all of the properties of the resource.

    """

    cols = [c['name'] for c in resource.columns() if c['name'] != 'year']

    header = None
    for r in doc.resources():
        
        if r.name == 'free_rp_meals':
            continue
        
        if not hasattr(r, 'year'):
            continue
        
        for d in r.iterdict:
            
            if header is None:
                yield ['year'] + list(d.keys())
          
            yield [r.year] + list(d.values())
            
            
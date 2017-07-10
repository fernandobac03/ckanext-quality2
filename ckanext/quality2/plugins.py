import ckan.plugins as p
from ckan.plugins.toolkit import add_template_directory

from ckanext.quality2 import validators



class QualityPlugin(p.SingletonPlugin):
    p.implements(p.IValidators)
    p.implements(p.IConfigurer)
    p.implements(p.IRoutes,inherit=True)

    def before_map(self, map):
	map.connect('add dataset', '/dataset/new',controller='ckanext.quality2.package:PackageController', action='new')          
        return map

    def after_map(self, map):
	map.connect('add dataset', '/dataset/new',controller='ckanext.quality2.package:PackageController', action='new')          
        return map


    def update_config(self, config):
        """
        
        """
        add_template_directory(config, 'theme/templates')
        p.toolkit.add_public_directory(config, 'theme/public')
        p.toolkit.add_resource('theme/public', 'ckanext-quality2')

    def get_validators(self):
        return {
            'repeating_text': validators.repeating_text,
            'repeating_text_output':
                validators.repeating_text_output,
            }



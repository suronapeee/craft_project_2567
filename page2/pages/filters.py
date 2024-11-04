# Import the template module from Django to create custom template filters
from django import template 

# Register the template filter so that it can be used in Django templates
register = template.Library()

# Define a custom filter called 'capitalize_words'
@register.filter    
def capitalize_words(value):
    # Split the input string into a list of words
    words = value.split()
    
    # Capitalize the first letter of each word and join them back into a string
    return ' '.join([word.capitalize() for word in words])

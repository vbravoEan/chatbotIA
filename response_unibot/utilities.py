from drf_yasg import openapi
 
def format_fact_sheet(fact_sheet_json):
        """
    Format software specifications into a human-readable fact sheet.
 
    This function takes a JSON object containing software specifications and
    formats it into a human-readable fact sheet. The fact sheet includes
    information about the project type, project subtype, purposes, benefits,
    characteristics, restrictions, and description.
 
    Args:
        fact_sheet_json (dict): A dictionary containing software specifications.
 
    Returns:
        str: A formatted fact sheet as a string.
 
    Example:
        fact_sheet = format_fact_sheet(fact_sheet_json)
    """
       
 
        fact_sheet = "\n\nMensaje: \n\n" + fact_sheet_json.get('Mensaje')
       
        return fact_sheet
   
description_property_schema = openapi.Schema(
    # Indica que el tipo de dato esperado es un objeto.
    type=openapi.TYPE_OBJECT,
    # Define las propiedades esperadas dentro del objeto.
    properties={
        'Respuesta': openapi.Schema(type=openapi.TYPE_STRING)
    }
)
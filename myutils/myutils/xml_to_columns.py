
# Function to parse XML and extract all items
def xml_to_columns(xml_string):
    # Namespace for schema
    ns = {'aw': 'http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/IndividualSurvey'}
    
    # Parse the XML string into a tree structure
    tree = ET.fromstring(xml_string)
    
    # Initialize a dictionary to store items, defaulting missing entries to None
    items = defaultdict(lambda: None)
    
    # Iterate through each element in the XML tree, using the namespace map
    for element in tree.findall('.//aw:*', namespaces=ns):
        # Extract the tag and remove the namespace information for clarity
        tag = element.tag.split('}')[-1]  
        # Store the element's text content under the tag in the items dictionary
        items[tag] = element.text
    
    return pd.Series(items)
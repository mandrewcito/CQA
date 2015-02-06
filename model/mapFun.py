mfInstantQuote = '''function(doc) {{
     	if (doc.type == 'InstantQuote' && doc.company == '{0}')
          emit(doc);
        }}'''

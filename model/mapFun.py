mfInstantQuote = '''function(doc) {{
     	if (doc.type == 'InstantQuote' && doc.company == '{0}' && doc.date >'{1}' && doc.date <'{2}')
          emit(doc);
        }}'''
mfInstantQuoteByDate = '''function(doc) {{
     	if (doc.type == 'InstantQuote' && doc.date >'{0}' && doc.date <'{1}')
          emit(doc);
        }}'''
mfBycompany = '''function(doc) {{
     	if (doc.type == '{0}' && doc.company == '{1}')
          emit(doc);
        }}'''

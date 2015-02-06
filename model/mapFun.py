mfInstantQuote = '''function(doc) {{
        var startTime=new Date();
        var endTime=new Date('{2}');
        var docTime=new Date();
     	if (doc.type == 'InstantQuote' && doc.company == '{0}' && doc.date >'{1}' && doc.date >'{2}')
          emit(doc);
        }}'''

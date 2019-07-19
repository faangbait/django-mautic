""" Do some stuff """

  obj, created = leads.objects.update_or_create(
    email=form.cleaned_data.get('contact')
  )

""" Do some other stuff """

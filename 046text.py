import textwrap

websitetext = '''
    Boris Johnson has warned European leaders there is “no prospect of a deal”
    unless they back down amid an intensifying row with Brussels before
    face-to-face talks with Angela Merkel in Berlin tomorrow.
    '''

print('No Dedent:')
print(textwrap.fill(websitetext))

print('Dedent:')
dedent_text = textwrap.dedent(websitetext).strip()
print(dedent_text)

print('Fill:')
print()
print(textwrap.fill(dedent_text, width=50))
print(textwrap.fill(dedent_text, width=100))

print('Controring Indent:')
print(textwrap.fill(dedent_text, initial_indent='   ', subsequent_indent='      '))

def to_lower_camel(string: str) -> str:
    if string == 'git_ssh_pull_link':
        return 'gitSSHPullLink'
    if string == 'public_url':
        return 'publicURL'
    
    camel_case = ''.join(word.capitalize() for word in string.split('_'))
    lower_camel_case = camel_case[0].lower() +  camel_case[1:]
    return lower_camel_case
from module.config.server import to_server


def upload_redirect(value):
    """
    redirect attr about upload.
    """
    if isinstance(value, list):
        if not value[0] and not value[1]:
            return 'do_not'
        elif value[0] and not value[1]:
            return 'save'
        elif not value[0] and value[1]:
            return 'upload'
        else:
            return 'save_and_upload'
    else:
        if not value:
            return 'do_not'
        else:
            return 'save'


def api_redirect(value):
    """
    redirect attr about api.
    """
    if value == 'auto':
        return 'default'
    elif to_server(value) == 'cn':
        return 'cn_gz_reverse_proxy'
    else:
        return 'default'


def dossier_redirect(value):
    """
    OpsiDossierBeacon -> AttackMode
    """
    if value:
        return 'current_dossier'
    else:
        return 'current'


def enhance_favourite_redirect(value):
    """
    EnhanceFavourite -> ShipToEnhance
    """
    if value:
        return 'all'
    else:
        return 'favourite'


def enhance_check_redirect(value):
    """
    CheckPerCategory should be at least 5
    """
    if isinstance(value, int):
        if value < 5:
            return 5
    return value

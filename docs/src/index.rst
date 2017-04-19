:github_url: https://www.github.com/ppokrovsky/pyvdp

======================================
PyVDP: VISA APIs. Wrapped with Python.
======================================

..  note::

    https://www.github.com/ppokrovsky/pyvdp

..  toctree::
    :maxdepth: 1
    :caption: Contents:

    intro
    data_and_analytics/index
    payment_methods/index
    risk_and_fraud/index
    glossary


++++++++++++
Installation
++++++++++++

..  code-block:: bash

    $ pip install pyvdp

+++++++++++++
Configuration
+++++++++++++

..  warning::

    Since configuration file contains sensitive data, such as user credentials, the configuration file itself and
    corresponding certificate/keyfiles should be kept safely and ignored by version control.

..  automodule:: pyvdp.configuration

+++++++
Logging
+++++++

..  warning::

    **DEBUG** should not be used in production environment because logs may (and will) contain sensitive data, such
    as VDP authentication credentials and card details.

..  automodule:: pyvdp.logger

=================
API Documentation
=================

..  toctree::
    :maxdepth: 1
    :caption: Contents:

    pyvdp/data_and_analytics/index
    pyvdp/payment_methods/index
    pyvdp/risk_and_fraud/index

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

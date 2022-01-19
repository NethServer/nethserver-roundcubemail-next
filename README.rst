========================
nethserver-roundcubemail-next
========================

Roundcube is a fast webmail client written in PHP. 

nethserver-roundcubemail-next is released in NethForge and it aims to follow last version of roundcubemail.
Nethserver-roundcubemail is designed to stick on LTS and will be conflicted by nethserver-roundcubemail-next.

You have to remove manually nethserver-roundcubemail before to install nethserver-roundcubemail-next

Database 
========

Configuration is saved in ``roundcubemail`` key inside ``configuration`` database.

Available properites:

* ``Server``: server address of the mail server, default is ``localhost``
* ``access``: can be ``public`` or ``private``, default is ``public``

  * *public*: webmail can be accessed from any networks
  * *private*: webmail can be accessed only from green interfaces and  trusted networks
* ``PluginsList``: comma separated list of enabled plugins, default is ``managesieve,markasjunk``.
  Before adding an option to this property, please be sure the plugin is already installed.
  A list of bundled plugins can be found inside file:``/usr/share/roundcubemail/plugins`` directory.
* ``skin``:  default is ``larry`` other skins can be found in ``/usr/share/roundcubemail/skins``
Example: ::

 roundcubemail=configuration
    PluginsList=managesieve,markasjunk
    Server=localhost
    access=private
    skin=larry


Configuration can be applied using the ``nethserver-roundcubemail-next-update`` event.


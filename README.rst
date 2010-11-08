wikidump...
===========

instructions to run::

        sudo apt-get install mediawiki
        sudo vim /etc/mediawiki/apache.conf

uncomment the following line::

        Alias /mediawiki /var/lib/mediawiki

restart apache::

        sudo /etc/init.d/apache2 restart

check that mediawiki works and configure the installation::

        firefox http://localhost/mediawiki/

some values I used (may be others)::

        wiki name: cdpedia
        admin password: secret

in the database configuration I used root and the password that I used during
installation, it may not be secure, but this wiki won't be public so...

finish installation::

        sudo cp /var/lib/mediawiki/config/LocalSettings.php /etc/mediawiki/

        firefox http://localhost/mediawiki

get this project::

        cd
        git clone https://github.com/Nassty/wikidump2htmlZombieMediaWiki.git
        cd wikidump2htmlZombieMediaWiki/
        sudo cp dumper.php /var/lib/mediawiki/

test it::

        curl -X POST http://localhost/mediawiki/dumper.php --data-binary '{{asd}}'


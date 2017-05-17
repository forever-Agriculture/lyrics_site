# DJANGO PROJECT MANAGER
# only for UNIX systems

help:
	@echo "REQUIREMENTS"
	@echo "  * nginx"
	@echo "  * django"
	@echo "  * supervisor"
	@echo "  * virtual environment"
	@echo ""
	@echo "USAGE"
	@echo "Start:"
	@echo "  - startproject - alternative django-admin.py startproject,"
	@echo "    but creates a project by the django-project-template structure."
	@echo "    ** Create a virtual environment and install Django."
	@echo ""
	@echo "Deploying the project:"
	@echo "  - make deploy - deploy project."
	@echo "    ** Create a configuration file: world/etc/local_settings.sh"
	@echo ""
	@echo "Main commands:"
	@echo "ONLY ON THE DEPLOYED PROJECT"
	@echo "  - make start - to start server."
	@echo "  - make stop - to stop server."
	@echo "  - make restart - to restart server."
	@echo "  - make status - show server status."
	@echo "  - make kill - forced to kill the server processes."
	@echo ""

# Start project.
startproject:
	django-admin.py startproject basic
	mkdir -p ./src/basic
	/bin/cp -rf ./basic/* ./src/
	rm -Rf ./basic

# Main commands:
all: start
runserver: start
start:
	sh ./world/bin/supervisorctl.sh --start

stop:
	sh ./world/bin/supervisorctl.sh --stop
	sh ./world/bin/killserver.sh

status:
	sh ./world/bin/supervisorctl.sh --status

forcekill: kill
kill:
	sh ./world/bin/killserver.sh

restart: stop start

forcestart:
	sh ./world/etc/init.d/runserver.sh

cleardebris:
	sh ./world/bin/cleardebris.sh

# Deploying the project:
deploy:
	sh ./world/bin/createconfigs.sh

lesscompiler:
	sh ./world/bin/lesscompiler.sh lib/ library/ import/ imports/ fonts/


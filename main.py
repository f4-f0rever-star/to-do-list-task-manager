from services.manager import ProjectManager

manager = ProjectManager()

# Add a new user if none exists
if not manager.get_user("Alex"):
    manager.add_user("Alex")

manager.add_project("Alex", "CLI Tool")
manager.add_project("Alex", "Another Project")

# Print all users and projects
for user in manager.users:
    print(f"User: {user.name}")
    for project in user.projects:
        print(f" Project: {project.title}")
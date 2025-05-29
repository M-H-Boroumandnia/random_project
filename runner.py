import os

project_structure = {
    ".": [
        "README.md",
        "requirements.txt",
        ".env.example",
        ".gitignore",
        "setup.py",
        {"config": ["__init__.py", "settings.py", "prompts.py"]},
        {"src": [
            "__init__.py",
            "cli.py",
            {"agent": [
                "__init__.py",
                "core.py",
                "conversation.py",
                "branching.py",
                "quality_scorer.py",
                "multi_session.py"
            ]},
            {"data": [
                "__init__.py",
                "models.py",
                "storage.py",
                "processor.py"
            ]},
            {"integrations": [
                "__init__.py",
                "llm_client.py",
                "platform_simulator.py",
                "sentiment.py"
            ]},
            {"reporting": [
                "__init__.py",
                "generator.py",
                "templates.py",
                "charts.py",
                "exporters.py"
            ]},
            {"utils": [
                "__init__.py",
                "display.py",
                "progress.py",
                "validators.py"
            ]}
        ]},
        {"data": [
            {"research_templates": [
                "customer_feedback.json",
                "product_research.json",
                "user_experience.json"
            ]},
            {"mock_users": [
                "personas.json",
                "profiles.json"
            ]},
            {"outputs": [
                {"conversations": []},
                {"reports": []},
                {"exports": []}
            ]}
        ]},
        {"tests": [
            "__init__.py",
            "test_agent.py",
            "test_cli.py",
            "test_conversation.py",
            {"fixtures": [
                "sample_conversations.json",
                "test_prompts.json"
            ]}
        ]},
        {"docs": [
            "CLI_USAGE.md",
            "DEMO_SCRIPT.md",
            "API_REFERENCE.md"
        ]}
    ]
}


def create_structure(base_path, structure):
    for item in structure:
        if isinstance(item, str):
            file_path = os.path.join(base_path, item)
            with open(file_path, "w") as f:
                if file_path.endswith(".py"):
                    f.write("# " + os.path.basename(file_path) + "\n")
        elif isinstance(item, dict):
            for folder, contents in item.items():
                folder_path = os.path.join(base_path, folder)
                os.makedirs(folder_path, exist_ok=True)
                create_structure(folder_path, contents)


def main():
    root_dir = "."
    os.makedirs(root_dir, exist_ok=True)
    create_structure(root_dir, project_structure[root_dir])
    print(f"Project structure for '{root_dir}' created successfully.")


if __name__ == "__main__":
    main()

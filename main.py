import argparse
import os
import sys
from pathlib import Path

import yaml


def get_project_name(cli_project: str | None = None) -> str:
    """
    Resolve project name with priority: CLI > env var > config file > auto-detect.
    
    Args:
        cli_project: Project name passed via CLI argument
        
    Returns:
        Resolved project name
        
    Raises:
        SystemExit: If no project can be resolved
    """
    # 1. CLI argument (highest priority)
    if cli_project:
        return cli_project
    
    # 2. Environment variable
    if env_project := os.environ.get("PROJECT_NAME"):
        return env_project
    
    # 3. Config file
    config_path = Path("config.yaml")
    if config_path.exists():
        with open(config_path) as f:
            config = yaml.safe_load(f)
            if config and config.get("project"):
                return config["project"]
    
    # 4. Auto-detect from src/ directory
    src_path = Path("src")
    if src_path.exists():
        projects = [
            d.name for d in src_path.iterdir() 
            if d.is_dir() and not d.name.startswith(("_", "."))
        ]
        if len(projects) == 1:
            return projects[0]
        elif len(projects) > 1:
            print(f"Multiple projects found in src/: {projects}")
            print("Please specify --project or set PROJECT_NAME env var")
            sys.exit(1)
    
    print("No project found. Please either:")
    print("  1. Use --project flag")
    print("  2. Set PROJECT_NAME environment variable")
    print("  3. Configure 'project' in config.yaml")
    print("  4. Create a project directory under src/")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Agentic Analytics Orchestrator")
    parser.add_argument('query', nargs='?', help="The business question or analysis task")
    parser.add_argument('--project', '-p', help="Project name under src/")
    parser.add_argument('--mode', choices=['plan', 'execute', 'review'], default='plan', help="Execution mode")
    
    args = parser.parse_args()
    
    # Resolve project name
    project_name = get_project_name(args.project)
    
    if not args.query:
        print(f"Welcome to Agentic Analytics.")
        print(f"Active project: {project_name}")
        print("Please provide a query or task.")
        sys.exit(0)

    print(f"Project: {project_name}")
    print(f"Query: {args.query}")
    print(f"Mode: {args.mode}")
    print("\nInitializing Agents...")
    # TODO: Initialize agents from src/{project_name}
    
    print("\nThinking...")
    # TODO: Orchestrate agent workflow
    
    print("\nDone.")


if __name__ == "__main__":
    main()

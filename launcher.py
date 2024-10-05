import subprocess
import sys
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the snake.py script
snake_script = os.path.join(current_dir, 'snake.py')

# Run the snake game
subprocess.run([sys.executable, snake_script])

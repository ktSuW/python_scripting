import os
import logging

# Script 1 : Manual Single Implementation with Explicit Class Hierarchy
class Logger:
    _instance = None
    
    @staticmethod
    def get_instance():
        if Logger._instance is None:
            Logger()
        return Logger._instance
    
    def __init__(self):
        if Logger._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            # logging.basicConfig(level=logging.INFO, format='%(asctime)s- %(levelname)s-%(message)s')
            logging.basicConfig(level=logging.INFO, format='%(message)s')
            Logger._instance=self 

class PointManager:
    """Manages loading and accessing points values of alphabets"""
    def __init__(self, filename):
        self.filename = filename
        self.points = self.load_points()
        
    def get_file_path(self):
        dir_path_for_file = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(dir_path_for_file, self.filename)

    def load_points(self):
        points = {}
        
        try:
            with open(self.get_file_path(), 'r') as file:
                for line in file:
                    if ":" in line:
                        letter, point = line.strip().split(":")
                        points[letter.strip()] = int(point.split()[0])
        except FileNotFoundError:
            logging.error("Error: The file does not exist.")
            raise SystemExit("File not found. Please ensure that the file is in the correct location.")
        except Exception as e:
            logging.error(f"An exepcted error occurred: {e}")
            raise SystemExit("Unexpected error occured...")
        return points 
    

class UserInteraction:
    """Handles interfactions with the user, process words, points, input and output"""
    
    def __init__(self, point_manager):
        self.point_manager = point_manager
    
    def get_user_input(self):
        words_scores_list = []
        total_points = 0 
        
        while True:
            word = input("Enter a word( or 'quit' to exit):").upper()
            if word == ("QUIT"):
                break 
            if not word.isalpha():
                logging.warning("Invalid input: Word must contain only alphabets.")
                continue 
            word_points = sum(self.point_manager.points.get(letter, 0) for letter in word)
            
            words_scores_list.append((word, word_points))
            total_points += word_points
            logging.info(f"{word}:{word_points}")
        return words_scores_list, total_points
            
    def print_total_points_summary(self, word_scores, total_points):
        print(f"\nSummary of entered words and their points")
        for i,(word,score) in enumerate(word_scores,1):
            print(f"{1}. {word}-{score}points")
        
        print(f"Total points: {total_points}")
        
class Application:
    """Main Application Class that orchestrate the exeuction of commands"""
    
    def __init__(self):
        self.point_manager = PointManager("points.txt")
        self.user_interaction = UserInteraction(self.point_manager)
    
    def run(self):
        word_scores, total_points = self.user_interaction.get_user_input()
        self.user_interaction.print_total_points_summary(word_scores, total_points)

if __name__ == "__main__":
    Logger.get_instance()
    app = Application()
    app.run()
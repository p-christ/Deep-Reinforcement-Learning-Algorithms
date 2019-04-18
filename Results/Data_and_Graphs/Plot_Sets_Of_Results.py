import pickle

from Config import Config
from Trainer import Trainer


trainer = Trainer(config=Config(), agents=None)



trainer.visualise_preexisting_results(save_image_path="Long_Corridor_Graph.png", data_path="Long_Corridor_Results_Data.pkl",
                                      title="Long Corridor", y_limits=(0.0, 0.25))


# trainer.visualise_set_of_preexisting_results(results_data_paths=["Cart_Pole_Results_Data.pkl",
#                                                                  "Mountain_Car_Results_Data.pkl"],
#                                              plot_titles=["Cart Pole (Discrete Actions)", "Mountain Car (Continuous Actions)"],
#                                              save_image_path="CartPole_and_MountainCar_Graph.png")


# trainer.visualise_set_of_preexisting_results(results_data_paths=["Data_and_Graphs/Bit_Flipping_Results_Data.pkl",
#                                                                  "Data_and_Graphs/Fetch_Reach_Results_Data.pkl"],
#                                              plot_titles=["Bit Flipping", "Fetch Reach"],
#                                              save_image_path="Data_and_Graphs/HER_Experiments.png")

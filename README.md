## SETUP

1. [Download](https://unity.com/download) and [install](https://docs.unity3d.com/hub/manual/InstallHub.html) Unity Hub along with Unity 2021.3.9f1 (LTS) or higher.

2. Install AutoDRIVE Simulator (from source):
     
    - Clone the Clone `AutoDRIVE-Simulator` branch of the `AutoDRIVE` repository:
    
      ```bash
      git clone --single-branch --branch AutoDRIVE-Simulator https://github.com/Tinker-Twins/AutoDRIVE.git
      ```
    - Launch Unity Hub and select `ADD` project button. Navigate to the download directory and select the parent folder of the `AutoDRIVE` repository.
  
    - Launch AutoDRIVE Simulator by running the project.
      > ***Note:*** *It may take several minutes to import and load the project for the first time. Please be patient.*

### Training
0. (Optional) Open the repository in a devcontainer:
  Install [dev containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
  Then Rebuild and Reopen in containers (in the vscode command palette, opened by ctrl/command+shift+p by default)

1. Start the training by sourcing the appropriate training configuration (using relative/global path) and `run-id`.
  
    ```bash
    uv run -- mlagents-learn Training\ Configurations/F1TenthRacing.yaml --run-id=run1
    ```

2. Hit the `Play` button in Unity Editor to "actually" start the training.

### Training Analysis

1. Navigate to the parent folder of [Results](https://github.com/Tinker-Twins/Computing-and-Simulation-for-Autonomy/tree/main/Project%20Workspace/Results) directory:
   
   ```bash
    cd <path/to/parent/folder/of/Results>
    ```

2. Launch TensorBoard to analyze the training results:
   
   ```
   tensorboard --logdir Results
   ```

3. Open browser application (tested with Google Chrome) and log on to http://localhost:6006 to view the training results.

    > ***Note:*** *You can view the training results "live" as the training happens, or choose to view it after the training is complete.*

### Deployment

1. Navigate to the `Results` directory and locate a folder named after the `<training_behaviour_name>/<run-id>` that you defined while training the agent(s).

2. In the inspector window, attach the saved neural network models (the `*.onnx` files) to the respective `Model` variable in the `BehaviourParameters` script attached to the agent(s).

3. Select `Default` or `Inference Only` mode in the `Behaviour Type` of the `BehaviourParameters` attached to the agent(s).

4. Hit the play button in Unity Editor and watch your agent(s) in autonomous mode!

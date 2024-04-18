# galaxywater_cnn_optimization
Code and dataset for Prediction of water positions on protein structure with artificial intelligence
Explanation of scripts:
- networks.py: Arechitecture of the 3D-CNN
- GWCNN_gpu.py: Code for training
- GWCNN_predict.py: Code to run prediction
Explanation of datasets:
- pdb/ - protein-water structures for the training and validation sets
- tests/ - protein-water structures for the standard test set
- new_test/ - protein-water structures for the additional test set

Pre-trained 3D-CNNs are available in ./trained_networks
To run training:
- python GWCNN_gpu.py
To run prediction:
- python GWCNN_predict.py path_to_input_pdb path_to_output_pdb

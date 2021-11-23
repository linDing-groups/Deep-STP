# Deep-STP
Comprehensive Assessment and Prediction of Snake Toxin Proteins Using Deep Learning Method
# Description
## Motivation
Snake venoms are mixtures of toxicological proteins. They play a substantial role in paralyzing and digestion of prey. Snake toxins mainly targets on the blood circulatory systems of the prey, as interruption in blood circulatory system makes the prey capitulate to the venom in a short period of time. In recent times, scientists derived many molecules from snake toxins which are used as a drug for treating hypertension and heart diseases. The research technologies on the basis of biochemistry are expensive, outdated and time consuming. Therefore, it is urgent to develop a computational tool that can accurately identify biomolecular functions in a short time.
## Results
we constructed a novel prediction model of its kind to predict snake toxin proteins. Their sequences were encoded by three types of features, namely natural vector, word 2 vector and g-gap di-peptide composition. Then, these features were optimized by using feature selection techniques. A classifier based on CNN was trained on the optimal features. The results of 10-fold cross-validation showed that our anticipated model would classify snake toxin proteins with accuracy of 91.26% and area under the curve of 0.965. On the independent dataset, our anticipated model could produce the accuracy of 90.18% which shows that our model could provide outstanding generalization ability.

## Required Packages

    Python3 (tested 3.5.4)
    jupyter (tested 1.0.0)
    scikit-learn (tested 0.22.1)
    pandas (tested 1.0.1)
    numpy (tested 1.18.1)
    gensim (tested 3.8.1)
    sklearn (tested 0.19.1)
    keras (tested 2.3.1)
    tensorflow (tested 2.1.0)

## create a new repository on the command line

### echo "# Deep-4mCGP" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/linDing-groups/Deep-4mCGP.git
git push -u origin main

## push an existing repository from the command line

git remote add origin https://github.com/linDing-groups/Deep-4mCGP.git
git branch -M main
git push -u origin main

## For Train the Model
    Train_CNN_Model.py

## Loading the Model
    Test.py
     
## Note

For files with different input sequences, you need to pay attention to the modification of parameters in code.

## Citation

Soon

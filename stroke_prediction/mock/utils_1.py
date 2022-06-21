import numpy as np
from joblib import load


class random_forest_model:
    def __init__(self):
        self.classifier = load('mock/model.sav')
    
    def clean_form(self,form):
        self.age = form['age']
        self.bmi = form['bmi']
        self.glucose = form['average_glucose_level']
        self.hypertension = form['hypertension']
        self.heartdisease = form['heartdisease']
        self.martial_status = form['martial_status']
        self.residence = form['residence']
        self.work_type = form['work_type']
        self.smoking_status = form['smoking_status']
        self.gender = form['gender']
        print("completed")

    def standardize(self,x, mean, std):
        return (x-mean)/std
    
    def standardize_values(self):
        self.age = self.standardize(self.age,54.844151, 22.220246)
        self.glucose = self.standardize(self.glucose, 118.795101, 55.288145)
        self.bmi = self.standardize(self.bmi, 29.549619, 6.867709)
    
    def label_heart_disease(self):
        if self.heartdisease == "yes":
            return 1
        else:
            return 0
    
    def label_hypertension(self):
        if self.hypertension == "yes":
            return 1
        else:
            return 0
    
    def label_married(self):
        if self.martial_status == "married":
            return 1
        else:
            return 0

    def label_residence(self):
        if self.residence == "urban":
            return 1
        else:
            return 0

    def encode_work_type(self):
        if(self.work_type == 'private'):
            return (1,0,0,0,0)
        elif(self.work_type == "self"):
            return(0,1,0,0,0)
        elif(self.work_type == "govt"):
            return(0,0,1,0,0)
        elif(self.work_type == 'child'):
            return(0,0,0,1,0)
        elif(self.work_type == 'never_worked'):
            return(0,0,0,0,1)    

    def encode_smoking(self):
        if(self.smoking_status == 'formerly'):
            return (1,0,0,0)
        elif(self.smoking_status == "never"):
            return(0,1,0,0)
        elif(self.smoking_status == "smokes"):
            return(0,0,1,0)
        elif(self.smoking_status == 'unknown'):
            return(0,0,0,1)

    def encode_gender(self):
        if(self.gender == 'male'):
            return (1,0,0)
        elif(self.gender == "female"):
            return(0,1,0)
        elif(self.gender == "other"):
            return(0,0,1)


    def preprocess(self):
        self.standardize_values()
        self.heart = self.label_heart_disease()
        self.tension = self.label_hypertension()
        self.married = self.label_married()
        self.residence = self.label_residence()
        self.private, self.self_emp, self.govt ,self.child, self.never = self.encode_work_type()
        self.formerly, self.never, self.smokes, self.unknown = self.encode_smoking()
        self.male, self.female, self.other = self.encode_gender()
        print("preprocess completed")
        
    def display(self):
        print(self.age, self.bmi, self.glucose)
        print(self.heart)
        print(self.tension)
        print(self.married)
        print(self.residence)
        print(self.private, self.self_emp, self.govt ,self.child, self.never)
        print(self.formerly, self.never, self.smokes, self.unknown)
        print(self.male, self.female, self.other)
        
    def create_array(self):
        self.X_test = np.array([self.age,self.tension,self.heart,self.married,
                                    self.residence,self.glucose,self.female,self.male,
                                    self.other,self.govt,self.never,self.private,self.self_emp,
                                    self.child,self.unknown,self.formerly,self.never,self.smokes,
                                    self.bmi])
        self.X_test = self.X_test.reshape(1,-1)

    def predict(self):
        self.create_array()
        classifier = self.classifier
        y_pred = classifier.predict(self.X_test)
        return y_pred

from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    feature_store_file_path:str
    train_file_path:str
    test_file_path:str


@dataclass
class DataValidationArtifact:
    report_file_path:str

@dataclass
class DataTransformationArtifact:
    transform_object_path:str
    transform_train_path:str
    transform_test_path:str
    transform_encoder_path:str

@dataclass
class DataTrainerArtifact:
    model_path:str
    r2_train_score:float
    r2_test_score:float





@dataclass
class ModelEvaluationArtifact:
    is_model_accepted:bool
    improved_accuracy:float
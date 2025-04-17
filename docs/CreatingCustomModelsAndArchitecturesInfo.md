# Conventions
- Each model/architecture file name should be in lowercase with underscores.
- Each class name should be in PascalCase.
- In factory classes, refer to the model/architecture name in lowercase with dashes.

Example (NewModelName):
- File: `rag/models/new_model_name.py`
- Class: `NewModelName`
- Name reference in factory: `new-model-name`
  ```python
  match model_name:  
      case "new-model-name":
            self.model = NewModelName(model_name, **kwargs)
  ```
 
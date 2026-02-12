from src.settings.base_settings import BaseProjectSettings


class _EnvironmentSettings(BaseProjectSettings): 
    ENVIRONMENT: str

EnvironmentSettings = _EnvironmentSettings()    
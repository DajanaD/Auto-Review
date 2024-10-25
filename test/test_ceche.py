import pytest
from app.utils.cache import cache_repo_content, get_cached_content
from app.main import redis

@pytest.mark.asyncio
async def test_cache_repo_content():
    key = "test_repo_content"
    value = {"files": [{"name": "test.py", "path": "src/test.py"}]}

    await cache_repo_content(key, value)

    cached_value = await get_cached_content(key)
    assert cached_value["files"][0]["name"] == "test.py"

@pytest.mark.asyncio
async def test_get_cached_content_not_found():
    key = "non_existent_key"
    cached_value = await get_cached_content(key)
    assert cached_value is None  # Должно вернуть None, если не найдено

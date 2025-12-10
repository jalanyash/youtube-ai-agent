import time
from functools import wraps

def retry_on_error(max_retries=3, delay=2):
    """
    Decorator to retry function on failure
    
    Args:
        max_retries: Maximum number of retry attempts
        delay: Seconds to wait between retries
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        print(f"   ⚠️ Attempt {attempt + 1} failed: {str(e)}")
                        print(f"   🔄 Retrying in {delay} seconds...")
                        time.sleep(delay)
                    else:
                        print(f"   ❌ All {max_retries} attempts failed")
            
            raise last_exception
        
        return wrapper
    return decorator


def safe_execute(func, default_return=None, error_message="Operation failed"):
    """
    Safely execute a function and return default on error
    
    Args:
        func: Function to execute
        default_return: Value to return on error
        error_message: Error message to display
        
    Returns:
        Function result or default_return on error
    """
    try:
        return func()
    except Exception as e:
        print(f"   ⚠️ {error_message}: {str(e)}")
        return default_return


# Test
if __name__ == "__main__":
    print("🧪 Testing Error Handler...\n")
    
    @retry_on_error(max_retries=3, delay=1)
    def test_function(should_fail=True):
        if should_fail:
            raise ValueError("Test error")
        return "Success!"
    
    # This will retry 3 times
    try:
        result = test_function(should_fail=True)
    except ValueError:
        print("✅ Retry logic working correctly!")
    
    # This will succeed
    result = test_function(should_fail=False)
    print(f"✅ Function result: {result}")
    
    print("\n✅ Error handling working!")
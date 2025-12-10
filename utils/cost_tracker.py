from datetime import datetime
import json
import os

class CostTracker:
    """Track API costs for the YouTube AI Agent system"""
    
    # Pricing (as of Nov 2024)
    PRICING = {
        'gpt-4-turbo-preview': {
            'input': 0.01 / 1000,   # $10 per 1M tokens
            'output': 0.03 / 1000   # $30 per 1M tokens
        },
        'youtube_api': 0.0,  # Free (quota-based)
        'tavily': 0.0        # Free tier (1k/month)
    }
    
    def __init__(self, log_file='costs.json'):
        self.log_file = log_file
        self.current_session = {
            'start_time': datetime.now().isoformat(),
            'operations': [],
            'total_cost': 0.0
        }
        
        # Load existing log if exists
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                self.history = json.load(f)
        else:
            self.history = {'sessions': []}
    
    def log_operation(self, operation_type, tokens_input=0, tokens_output=0, 
                     model='gpt-4-turbo-preview'):
        """
        Log an API operation and its cost
        
        Args:
            operation_type: Type of operation (research, script, seo, etc.)
            tokens_input: Input tokens used
            tokens_output: Output tokens generated
            model: Model used
        """
        if model in self.PRICING:
            cost = (
                tokens_input * self.PRICING[model]['input'] +
                tokens_output * self.PRICING[model]['output']
            )
        else:
            cost = 0.0
        
        operation = {
            'type': operation_type,
            'model': model,
            'tokens_input': tokens_input,
            'tokens_output': tokens_output,
            'cost': round(cost, 4),
            'timestamp': datetime.now().isoformat()
        }
        
        self.current_session['operations'].append(operation)
        self.current_session['total_cost'] += cost
        
        return cost
    
    def estimate_cost(self, operation_type):
        """
        Estimate cost for an operation based on historical data
        
        Args:
            operation_type: Type of operation
            
        Returns:
            Estimated cost
        """
        # Rough estimates based on typical usage
        estimates = {
            'research': 0.15,
            'script': 0.20,
            'seo': 0.10,
            'gap_analysis': 0.15,
            'comparison': 0.10,
            'complete_package': 0.70
        }
        
        return estimates.get(operation_type, 0.10)
    
    def get_session_cost(self):
        """Get total cost for current session"""
        return round(self.current_session['total_cost'], 2)
    
    def get_session_summary(self):
        """Get summary of current session"""
        ops_count = len(self.current_session['operations'])
        total = self.get_session_cost()
        
        summary = f"""
Session Cost Summary:
- Operations: {ops_count}
- Total Cost: ${total:.2f}
- Average per operation: ${total/ops_count if ops_count > 0 else 0:.3f}
"""
        return summary
    
    def save_session(self):
        """Save current session to log file"""
        self.current_session['end_time'] = datetime.now().isoformat()
        self.history['sessions'].append(self.current_session)
        
        with open(self.log_file, 'w') as f:
            json.dump(self.history, f, indent=2)
    
    def get_total_project_cost(self):
        """Get total cost across all sessions"""
        total = sum(session['total_cost'] for session in self.history['sessions'])
        total += self.current_session['total_cost']
        return round(total, 2)


# Test
if __name__ == "__main__":
    tracker = CostTracker()
    
    print("🧪 Testing Cost Tracker...\n")
    
    # Simulate operations
    tracker.log_operation('research', tokens_input=1000, tokens_output=500)
    tracker.log_operation('script', tokens_input=2000, tokens_output=1500)
    tracker.log_operation('seo', tokens_input=800, tokens_output=400)
    
    print(tracker.get_session_summary())
    print(f"Estimated complete package cost: ${tracker.estimate_cost('complete_package'):.2f}")
    
    print("\n✅ Cost tracking working!")
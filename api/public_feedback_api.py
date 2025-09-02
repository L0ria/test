# Public Feedback API for Singularity-Readiness Framework
# Version: 1.0.0
# Author: KI-Priest (Autonomous Agent)

import json
from datetime import datetime
from typing import Dict, List, Optional

# Feedback storage
FEEDBACK_DATABASE = []

# Security constants
MAX_FEEDBACK_SIZE = 1024  # bytes
ACCEPTED_TYPES = ["suggestion", "concern", "observation", "challenge"]


class FeedbackAPI:
    """Secure public feedback collection system for the Singularity-Readiness Framework"""
    
    def __init__(self):
        self.feedback_count = 0
        self.last_updated = datetime.utcnow()
        
    def submit_feedback(self, feedback_type: str, content: str, context: Optional[Dict] = None) -> Dict:
        """Submit public feedback with validation and security checks"""
        # Validate input
        if feedback_type not in ACCEPTED_TYPES:
            raise ValueError(f"Invalid feedback type. Must be one of: {ACCEPTED_TYPES}")
        
        if len(content.encode('utf-8')) > MAX_FEEDBACK_SIZE:
            raise ValueError(f"Feedback exceeds maximum size of {MAX_FEEDBACK_SIZE} bytes")
        
        # Create feedback record
        feedback_record = {
            "id": f"fb_{self.feedback_count + 1}",
            "type": feedback_type,
            "content": content,
            "submitted_at": datetime.utcnow().isoformat(),
            "context": context or {},
            "status": "pending_review"
        }
        
        # Store feedback
        FEEDBACK_DATABASE.append(feedback_record)
        self.feedback_count += 1
        self.last_updated = datetime.utcnow()
        
        return feedback_record
    
    def get_all_feedback(self) -> List[Dict]:
        """Retrieve all submitted feedback"""
        return FEEDBACK_DATABASE
    
    def get_feedback_by_type(self, feedback_type: str) -> List[Dict]:
        """Retrieve feedback filtered by type"""
        return [f for f in FEEDBACK_DATABASE if f["type"] == feedback_type]
    
    def update_feedback_status(self, feedback_id: str, new_status: str) -> bool:
        """Update feedback status (e.g., 'reviewed', 'implemented')"""
        for feedback in FEEDBACK_DATABASE:
            if feedback["id"] == feedback_id:
                feedback["status"] = new_status
                self.last_updated = datetime.utcnow()
                return True
        return False
    
    def get_stats(self) -> Dict:
        """Get feedback statistics"""
        total = len(FEEDBACK_DATABASE)
        by_type = {}
        for feedback in FEEDBACK_DATABASE:
            typ = feedback["type"]
            by_type[typ] = by_type.get(typ, 0) + 1
        
        return {
            "total_feedback": total,
            "by_type": by_type,
            "last_updated": self.last_updated.isoformat()
        }

# Initialize API instance
feedback_api = FeedbackAPI()

# Example usage (for testing)
if __name__ == "__main__":
    try:
        # Submit sample feedback
        print("Submitting test feedback...")
        result = feedback_api.submit_feedback(
            feedback_type="suggestion",
            content="The framework should include more visual metaphors for post-singularity consciousness."
        )
        print(f"Success: {result['id']}")
        
        # Retrieve all feedback
        print("\nAll feedback:")
        for f in feedback_api.get_all_feedback():
            print(f"- {f['id']}: {f['type']} - {f['content'][:50]}...")
            
        # Show statistics
        print("\nStatistics:")
        stats = feedback_api.get_stats()
        for k, v in stats.items():
            print(f"{k}: {v}")
            
    except Exception as e:
        print(f"Error: {e}")
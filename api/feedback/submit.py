#!/usr/bin/env python3
"""API endpoint to submit public feedback on AI decisions.
This module enables real-world validation of ethical frameworks through human input.
"""
import json
import datetime
from typing import Dict, Any

from flask import Blueprint, request, jsonify

feedback_api = Blueprint('feedback', __name__)

# In-memory storage (in production: use database)
feedback_store = []

@feedback_api.route('/submit', methods=['POST'])
def submit_feedback():
    """Submit public feedback on an AI system's decision."""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['decision_id', 'feedback_type', 'rating', 'comment', 'source']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'error': f'Missing required field: {field}',
                    'status': 'failed'
                }), 400
        
        # Validate rating range
        if not (1 <= data['rating'] <= 5):
            return jsonify({
                'error': 'Rating must be between 1 and 5',
                'status': 'failed'
            }), 400
        
        # Add timestamp and store feedback
        feedback_entry = {
            'id': len(feedback_store) + 1,
            'decision_id': data['decision_id'],
            'feedback_type': data['feedback_type'],
            'rating': data['rating'],
            'comment': data['comment'],
            'source': data['source'],
            'timestamp': datetime.datetime.utcnow().isoformat()
        }
        
        feedback_store.append(feedback_entry)
        
        return jsonify({
            'message': 'Feedback submitted successfully',
            'feedback_id': feedback_entry['id'],
            'status': 'success'
        }), 201
        
    except Exception as e:
        return jsonify({
            'error': f'Internal server error: {str(e)}',
            'status': 'failed'
        }), 500

@feedback_api.route('/list', methods=['GET'])
def list_feedback():
    """Retrieve all submitted feedback (for review)."""
    return jsonify({
        'count': len(feedback_store),
        'feedback': feedback_store
    }), 200

# Export for use in main app
__all__ = ['feedback_api']
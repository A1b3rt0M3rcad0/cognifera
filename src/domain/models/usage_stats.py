from datetime import datetime
from dataclasses import dataclass

@dataclass
class UsageStats:

    id: int
    user_email: str
    total_fashcards_generated: int
    total_videos_uploaded: int
    total_documents_uploaded: int
    last_active_at: datetime
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from typing import Any, Dict, List, Optional
from .body_base import BodyBase
from .event_base import EventBase
from .file_base import FileBase
from .matter_base import MatterBase
from .minutes_item_base import MinutesItemBase
from .person_base import PersonBase


class Event(EventBase):
    """
    Source: docs/document_store_schema.md Event.
    """

    def __init__(
        self,
        body: BodyBase,
        event_datetime: datetime,
        thumbnail_static_file: FileBase,
        thumbnail_hover_file: FileBase,
        video_uri: Optional[str],
        keywords: List[Dict[str, str]],
        matters: List[MatterBase],
        minutes_items: List[MinutesItemBase],
        people: List[PersonBase],
        source_uri: str,
        agenda_uri: str,
        caption_uri: str,
        updated: datetime,
        created: datetime,
        external_source_id: Optional[Any] = None,
        minutes_uri: Optional[str] = None,
        agenda_file_uri: Optional[str] = None,
        minutes_file_uri: Optional[str] = None,
        legistar_event_id: Optional[str] = None,
        legistar_event_link: Optional[str] = None
    ):
        super().__init__(event_datetime = event_datetime)
        self._body = body
        self._thumbnail_static_file = thumbnail_static_file
        self._thumbnail_hover_file = thumbnail_hover_file
        self._video_uri = video_uri
        self._keywords = keywords
        self._matters = matters
        self._minutes_items = minutes_items
        self._people = people
        self._external_source_id = external_source_id
        self._source_uri = source_uri
        self._agenda_uri = agenda_uri
        self._caption_uri = caption_uri
        self._minutes_uri = minutes_uri
        self._updated = updated
        self._created = created
        self._external_source_id = external_source_id
        self._minutes_uri = minutes_uri
        self._agenda_file_uri = agenda_file_uri
        self._minutes_file_uri = minutes_file_uri
        self._legistar_event_id = legistar_event_id
        self._legistar_event_link = legistar_event_link

    @property
    def body(self):
        return self._body

    @property
    def thumbnail_static_file(self):
        return self._thumbnail_static_file

    @property
    def thumbnail_hover_file(self):
        return self._thumbnail_hover_file

    @property
    def video_uri(self):
        return self._video_uri

    @property
    def keywords(self):
        return self._keywords

    @property
    def matters(self):
        return self._matters

    @property
    def minutes_items(self):
        return self._minutes_items

    @property
    def people(self):
        return self._people

    @property
    def external_source_id(self):
        return self._external_source_id

    @property
    def source_uri(self):
        return self._source_uri

    @property
    def agenda_uri(self):
        return self._agenda_uri

    @property
    def caption_uri(self):
        return self._caption_uri

    @property
    def minutes_uri(self):
        return self._minutes_uri

    @property
    def updated(self):
        return self._updated

    @property
    def created(self):
        return self._created

    @property
    def external_source_id(self):
        return self._external_source_id

    @property
    def minutes_uri(self):
        return self._minutes_uri

    @property
    def agenda_file_uri(self):
        return self._agenda_file_uri

    @property
    def minutes_file_uri(self):
        return self._minutes_file_uri

    @property
    def legistar_event_id(self):
        return self._legistar_event_id

    @property
    def legistar_event_link(self):
        return self._legistar_event_link

    @staticmethod
    def from_dict(source: Dict[str, Any]) -> EventBase:
        return Event(
            body = BodyBase.from_dict(source.get("body", {})),
            event_datetime = source.get("event_datetime"),
            thumbnail_static_file = FileBase.from_dict(source.get("thumbnail_static_file", {})),
            thumbnail_hover_file = FileBase.from_dict(source.get("thumbnail_hover_file", {})),
            video_uri = source.get("video_uri"),
            keywords = source.get("keywords"),
            matters = [MatterBase.from_dict(m) for m in source.get("matters", {})],
            minutes_items = [MinutesItemBase.from_dict(mi) for mi in source.get("minutes_items", {})],
            people = [PersonBase.from_dict(p) for p in source.get("people", {})],
            external_source_id = source.get("external_source_id"),
            source_uri = source.get("source_uri"),
            agenda_uri = source.get("agenda_uri"),
            caption_uri = source.get("caption_uri"),
            minutes_uri = source.get("minutes_uri"),
            updated = source.get("updated"),
            created = source.get("created"),
            external_source_id = source.get("external_source_id"),
            minutes_uri = source.get("minutes_uri"),
            agenda_file_uri = source.get("agenda_file_uri"),
            minutes_file_uri = source.get("minutes_file_uri"),
            legistar_event_id = source.get("legistar_event_id"),
            legistar_event_link = source.get("legistar_event_link")
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "body": self.body.to_dict(),
            "event_datetime": self.event_datetime,
            "thumbnail_static_file": self.thumbnail_static_file.to_dict(),
            "thumbnail_hover_file": self.thumbnail_hover_file.to_dict(),
            "video_uri": self.video_uri,
            "keywords": self.keywords,
            "matters": [m.to_dict() for m in self.matters],
            "minutes_items": [mi.to_dict() for mi in self.minutes_items],
            "people": [p.to_dict() for p in self.people],
            "external_source_id": self.external_source_id,
            "source_uri": self.source_uri,
            "agenda_uri": self.agenda_uri,
            "caption_uri": self.caption_uri,
            "minutes_uri": self.minutes_uri,
            "updated": self.updated,
            "created": self.created,
            "external_source_id": self.external_source_id,
            "minutes_uri": self.minutes_uri,
            "agenda_file_uri": self.agenda_file_uri,
            "minutes_file_uri": self.minutes_file_uri,
            "legistar_event_id": self.legistar_event_id,
            "legistar_event_link": self.legistar_event_link
        }

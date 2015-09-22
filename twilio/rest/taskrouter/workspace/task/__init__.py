# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource
from twilio.rest.v2010.workspace.task.reservation import ReservationList


class TaskList(ListResource):

    def __init__(self, domain, workspace_sid):
        super(TaskList, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'workspace_sid': workspace_sid,
        }
        self._uri = "/Workspaces/{workspace_sid}/Tasks".format(**self._instance_kwargs)

    def read(self, priority=values.unset, assignment_status=values.unset,
             workflow_sid=values.unset, workflow_name=values.unset,
             task_queue_sid=values.unset, task_queue_name=values.unset, limit=None,
             page_size=None, **kwargs):
        limits = self._domain.read_limits(limit, page_size)
        
        params = values.of({
            "Priority": priority,
            "AssignmentStatus": assignment_status,
            "WorkflowSid": workflow_sid,
            "WorkflowName": workflow_name,
            "TaskQueueSid": task_queue_sid,
            "TaskQueueName": task_queue_name,
        })
        params.update(kwargs)
        
        return self._domain.read(
            self,
            TaskInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, priority=values.unset, assignment_status=values.unset,
             workflow_sid=values.unset, workflow_name=values.unset,
             task_queue_sid=values.unset, task_queue_name=values.unset,
             page_token=None, page=None, page_size=None, **kwargs):
        params = values.of({
            "Priority": priority,
            "AssignmentStatus": assignment_status,
            "WorkflowSid": workflow_sid,
            "WorkflowName": workflow_name,
            "TaskQueueSid": task_queue_sid,
            "TaskQueueName": task_queue_name,
        })
        params.update(kwargs)
        
        return self._domain.page(
            self,
            TaskInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, attributes, workflow_sid, timeout=values.unset,
               priority=values.unset):
        data = values.of({
            "Attributes": attributes,
            "WorkflowSid": workflow_sid,
            "Timeout": timeout,
            "Priority": priority,
        })
        
        return self._domain.create(
            TaskInstance,
            self._instance_kwargs,
            'POST',
            self._uri,
            data=data,
        )


class TaskContext(InstanceContext):

    def __init__(self, domain, workspace_sid, sid):
        super(TaskContext, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'workspace_sid': workspace_sid,
            'sid': sid,
        }
        self._uri = "/Workspaces/{workspace_sid}/Tasks/{sid}".format(**self._instance_kwargs)
        
        # Dependents
        self._reservations = None

    def fetch(self):
        return self._domain.fetch(
            TaskInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
        )

    def update(self, attributes=values.unset, assignment_status=values.unset,
               reason=values.unset, priority=values.unset):
        data = values.of({
            "Attributes": attributes,
            "AssignmentStatus": assignment_status,
            "Reason": reason,
            "Priority": priority,
        })
        
        return self._domain.update(
            TaskInstance,
            self._instance_kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def delete(self):
        return self._domain.delete("delete", self._uri)

    @property
    def reservations(self):
        if self._reservations is None:
            self._reservations = ReservationList(
                self._domain,
                workspace_sid=self._instance_kwargs['workspace_sid'],
                task_sid=self._instance_kwargs['sid'],
            )
        return self._reservations


class TaskInstance(InstanceResource):

    def __init__(self, domain, payload, workspace_sid, sid=None):
        super(TaskInstance, self).__init__(domain)
        
        # Marshaled Properties
        self._account_sid = payload['account_sid']
        self._age = payload['age']
        self._assignment_status = payload['assignment_status']
        self._attributes = payload['attributes']
        self._date_created = deserialize.iso8601_datetime(payload['date_created'])
        self._date_updated = deserialize.iso8601_datetime(payload['date_updated'])
        self._priority = payload['priority']
        self._reason = payload['reason']
        self._sid = payload['sid']
        self._task_queue_sid = payload['task_queue_sid']
        self._timeout = payload['timeout']
        self._workflow_sid = payload['workflow_sid']
        self._workspace_sid = payload['workspace_sid']
        
        # Context
        self._lazy_context = None
        self._context_workspace_sid = workspace_sid
        self._context_sid = sid or self._sid

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = TaskContext(
                self._domain,
                self._context_workspace_sid,
                self._context_sid,
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._account_sid

    @property
    def age(self):
        """ The age """
        return self._age

    @property
    def assignment_status(self):
        """ The assignment_status """
        return self._assignment_status

    @property
    def attributes(self):
        """ The attributes """
        return self._attributes

    @property
    def date_created(self):
        """ The date_created """
        return self._date_created

    @property
    def date_updated(self):
        """ The date_updated """
        return self._date_updated

    @property
    def priority(self):
        """ The priority """
        return self._priority

    @property
    def reason(self):
        """ The reason """
        return self._reason

    @property
    def sid(self):
        """ The sid """
        return self._sid

    @property
    def task_queue_sid(self):
        """ The task_queue_sid """
        return self._task_queue_sid

    @property
    def timeout(self):
        """ The timeout """
        return self._timeout

    @property
    def workflow_sid(self):
        """ The workflow_sid """
        return self._workflow_sid

    @property
    def workspace_sid(self):
        """ The workspace_sid """
        return self._workspace_sid

    def fetch(self):
        self._context.fetch()

    def update(self, attributes=values.unset, assignment_status=values.unset,
               reason=values.unset, priority=values.unset):
        self._context.update(
            attributes=attributes,
            assignment_status=assignment_status,
            reason=reason,
            priority=priority,
        )

    def delete(self):
        self._context.delete()

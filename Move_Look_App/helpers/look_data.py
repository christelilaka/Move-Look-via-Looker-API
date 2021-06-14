class Look:
    def __init__(self, data):
        self._title = data.title
        self._description = data.description
        self._model = data.query.model
        self._view = data.query.view
        self._fields = data.query.fields
        self._pivots = data.query.pivots
        self._fill_fields = data.query.fill_fields
        self._filters = data.query.filters
        self._filter_expression = data.query.filter_expression
        self._sorts = data.query.sorts
        self._limit = data.query.limit
        self._column_limit = data.query.column_limit
        self._total = data.query.total
        self._row_total = data.query.row_total
        self._subtotals = data.query.subtotals
        self._vis_config = data.query.vis_config
        self._filter_config = data.query.filter_config
        self._visible_ui_sections = data.query.visible_ui_sections
        self._dynamic_fields = data.query.dynamic_fields
        self._query_timezone = data.query.query_timezone
        self._user_id = data.user.id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def model(self):
        return self._model
    @property
    def view(self):
        return self._view
        
    @property
    def fields(self):
        return self._fields

    @property
    def pivots(self):
        return self._pivots

    @property
    def fill_fields(self):
        return self._fill_fields

    @property
    def filters(self):
        return self._filters
    
    @property
    def filter_expression(self):
        return self._filter_expression
    
    @property
    def sorts(self):
        return self._sorts
    
    @property
    def limit(self):
        return self._limit

    @property
    def column_limit(self):
        return self._column_limit

    @property
    def total(self):
        return self._total 

    @property
    def row_total(self):
        return self._row_total

    @property
    def subtotals(self):
        return self._subtotals

    @property
    def vis_config(self):
        return self._vis_config

    @property
    def filter_config(self):
        return self._filter_config

    @property
    def visible_ui_sections(self):
        return self._visible_ui_sections

    @property
    def dynamic_fields(self):
        return self._dynamic_fields

    @property
    def query_timezone(self):
        return self._query_timezone

    @property
    def user_id(self):
        return self._user_id
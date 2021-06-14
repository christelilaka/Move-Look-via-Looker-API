import looker_sdk
from .look_data import Look

models = looker_sdk.sdk.api31.models

class MoveLook():
    def __init__(self, new_instance, old_instance, look_id) -> None:
        self._look_id = look_id
        self._new_instance = new_instance
        self._old_instance = old_instance

    def move(self):
        # Get Look info and User's email from old instance
        look = Look(data = self._old_instance.look(self._look_id))
        user_info = self._old_instance.user(user_id = look.user_id)

        # Calls to new instance
        new_user_info = self._new_instance.search_users(fields = "id, personal_space_id, personal_folder_id", email = user_info.email)
        folder = self._new_instance.folder(folder_id = str(new_user_info[0].personal_folder_id), fields="name, parent_id, id")

        # Create query on new instance
        query = self._new_instance.create_query(
                    body = models.WriteQuery(
                        model = look.model,
                        view = look.view,
                        fields = look.fields,
                        pivots = look.pivots,
                        fill_fields = look.fill_fields, 
                        filters = look.filters,
                        filter_expression = look.filter_expression,
                        sorts = look.sorts, 
                        limit = look.limit, 
                        column_limit = look.column_limit,
                        total = look.total,
                        row_total = look.row_total,
                        subtotals = look.subtotals,
                        vis_config = look.vis_config, 
                        filter_config = look.filter_config,
                        visible_ui_sections = look.visible_ui_sections,
                        dynamic_fields = look.dynamic_fields,
                        query_timezone = look.query_timezone))

        # Create Look on new instance
        self._new_instance.create_look(
            body = models.WriteLookWithQuery(
                title = look.title,
                description = look.description,
                is_run_on_load = True,
                query_id = query.id,
                folder = models.WriteFolderBase(name = folder.name, parent_id = folder.parent_id),
                folder_id = folder.id,
                user_id = new_user_info[0].id,
                space_id = folder.id,
                space = models.WriteSpaceBase(name = folder.name, parent_id = folder.parent_id),
                query = models.WriteQuery(
                    model = look.model,
                    view = look.view,
                    fields = look.fields,
                    pivots = look.pivots,
                    fill_fields = look.fill_fields,
                    filters = look.filters,
                    filter_expression = look.filter_expression,
                    sorts = look.sorts,
                    limit = look.limit,
                    column_limit = look.column_limit,
                    total = look.total,
                    row_total = look.row_total,
                    subtotals = look.subtotals,
                    vis_config = look.vis_config,
                    filter_config = look.filter_config,
                    visible_ui_sections = look.visible_ui_sections,
                    dynamic_fields = look.dynamic_fields,
                    query_timezone = look.query_timezone)))
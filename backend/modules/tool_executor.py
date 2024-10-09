# backend/modules/tool_executor.py

from tools import db_tools

class ToolExecutor:
    def __init__(self):
        pass

    def execute_tool(self, tool_name: str, params: dict):
        tool_functions = {
            "apply_coupon": db_tools.apply_coupon,
            "get_transactions": db_tools.get_transactions,
            "post_transaction": db_tools.post_transaction,
            "update_transaction": db_tools.update_transaction,
            "delete_transaction": db_tools.delete_transaction,
            "sales_summary": db_tools.sales_summary,
            "revenue_analysis": db_tools.revenue_analysis,
            "get_customers": db_tools.get_customers,
            "update_customer_info": db_tools.update_customer_info,
            "customer_purchase_history": db_tools.customer_purchase_history,
            "get_items": db_tools.get_items,
            "update_item": db_tools.update_item,
            "list_stores": db_tools.list_stores,
            "store_performance": db_tools.store_performance,
            "create_manage_coupons": db_tools.create_manage_coupons,
        }

        if tool_name in tool_functions:
            return tool_functions[tool_name](**params)
        else:
            raise Exception(f"Tool {tool_name} not found.")
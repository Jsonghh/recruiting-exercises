# -*- coding: utf-8 -*-
'''
# Created on Nov-18-19 15:28
# InventoryAllocator.py
# @author: Jiesong He
'''


class InventoryAllocator:
    def __init__(self):
        pass

    def inventory_allocator(self, order, warehouses):
        # early exist for invalid input data
        if not order or not warehouses:
            return []

        ans = []
        # iterate in the warehouses and find the amount to be shipped
        for warehouse in warehouses:
            wh_name, inventory = warehouse['name'], warehouse['inventory']
            map_for_current_wh = {wh_name : {}}
            for wh_obj, wh_amount in inventory.items():
            
                # find how many objects to deliver by iterating order map
                # if the amount needed for an object is 0, we skip it 
                if wh_obj in order and order[wh_obj]:
                    amount_to_go = min(wh_amount, order[wh_obj])
                    order[wh_obj] -= amount_to_go
                    map_for_current_wh[wh_name][wh_obj] = amount_to_go

            # if no object is required from the current warehouse, we don't add the map_for_current_wh
            # into ans, otherwise append map_for_current_wh in the ans
            if not map_for_current_wh[wh_name]:
                continue
            ans.append(map_for_current_wh)

        # before returning ans, check if the amount required to be shipped is zero for each obj in the order map
        for amount_required in order.values():
            if amount_required:
                return []

        return ans

    

        
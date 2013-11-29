"""
This is the sample code from the coolstuffinoneplace.co.uk website.

def homepage:  This function returns the list of items to display on the landing page.
                On the landing page, we will be displaying only the latest 3 items with high ranking 
                from the past 2 weeks and any other items before that based on the rank.
                This function gets called each time everytime user scrolls on the page.
                
                The database request to get all the items is called only once.
                Each time user scrolls on the page, we use the items from the list
                that are already retrieved and display them
                
def gadget_category : This function returns the list of items classes as gadgets.
                      This function gets called when user clicks on the gadgets tab on the menu.
"""

NEW_ITEM_DISPLAY_RANGE_DAYS = 14


@cache_page(60 * 60 * 24)
def homepage(request):
    """
    This function gets called when a user open the main page of the website for the first
    time. By default users are taken to the homepage where we show the most popular items
    on the website
    """

    new_date = date.today() - timedelta(days=NEW_ITEM_DISPLAY_RANGE_DAYS)

    # Get the items that are most viewed by users
    most_viewd_list = CoolStuff.objects.filter(show_on_website=True).order_by('-item_rank')
    
    # Get only 3 items from the list of items that are created in the last 14 days
    new_list = most_viewd_list.filter(date_created__gte=new_date).order_by('-date_created')[0:3]
    
    # From the most viewed list, exclude the items that are added recently
    most_viewd_list = most_viewd_list.exclude(date_created__gte=new_date)
    
    # Our list of items to display on the homepage contains latest 3 items that are inserted
    # in the past 14 days and anything else before that based on the most views.
    item_list = list(chain(new_list, most_viewd_list))

    # Split the items into 3 seperate lists for 3 coloumns on the browser
    column_1_items_list, column_2_items_list, column_3_items_list = [item_list[i::3]for i in range(3)]

    template = 'homepage.html'
    page_template = 'home_page_index.html'

    # If the user is scrolling on the page, use only the page_template, which contains only the
    # details of items to display on the page (not the menu or search etc)
    if request.is_ajax():
        template = page_template

    return render_to_response(template,
                        {'page_template': page_template,
                         'column_1_items_list': column_1_items_list,
                         'column_2_items_list': column_2_items_list,
                         'column_3_items_list': column_3_items_list,
                         'register_form': header_register_form},
                        context_instance=RequestContext(request))
                        
  
@cache_page(60 * 60 * 24)
def gadget_category(request):
    """
    Displays all the cool gadget items
    Gets called when user clicks on Gadgets menu item.
    """
    gadget_list = CoolStuff.objects.filter(gadget_type=True).filter(show_on_website=True).order_by('-item_rank')
    column_1_category_items, column_2_category_items, column_3_category_items = [gadget_list[i::3]for i in range(3)]

    template = 'category.html'
    page_template = 'category_index.html'

    # If the user is scrolling on the page, use only the page_template, which contains only the
    # details of items to display on the page (not the menu or search etc)
    if request.is_ajax():
        template = page_template

    return render_to_response(template,
            {'page_template': page_template,
            'column_1_category_items': column_1_category_items,
            'column_2_category_items': column_2_category_items,
            'column_3_category_items': column_3_category_items,
             'current_category': 'gadgets',
             'register_form': header_register_form},
           context_instance=RequestContext(request))  

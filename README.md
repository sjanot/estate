# The Real Estate Advertisement module

Application for real estate, register of properties with offers, details, settings

# Real estate - account

Connection between real estate and account module

## Chapter 2: A New Application
**Exercise 2.1**
```
Create the required addon files.

Create the following folders and files:

/home/$USER/src/tutorials/estate/__init__.py

/home/$USER/src/tutorials/estate/__manifest__.py

The __manifest__.py file should only define the name and the dependencies of our modules. The only necessary 
framework module for now is base.
```
**Exercise 2.2**
```
Make your module an ‘App’.

Add the appropriate key to your __manifest__.py so that the module appears when the ‘Apps’ filter is on.
```
## Chapter 3: Models And Basic Fields

**Exercise 3.1**
```
Define the real estate properties model.

Based on example given in the CRM module, create the appropriate files and folder for the estate_property table.

When the files are created, add a minimum definition for the estate.property model.
```
**Exercise 3.2**
```
Add a description.

Add a _description to your model to get rid of one of the warnings.
```
**Exercise 3.3**
```
Add basic fields to the Real Estate Property table.

Add the following basic fields to the table:

Field               Type    
name                Char
description         Text
postcode            Char
date_availability   Date
expected_price      Float
selling_price       Float
bedrooms            Integer
living_area         Integer
facades             Integer
garage              Boolean
garden              Boolean
garden_area         Integer
garden_orientation  Selection

The garden_orientation field must have 4 possible values: ‘North’, ‘South’, ‘East’ and ‘West’. 
The selection list is defined as a list of tuples, see here for an example.
```
**Exercise 3.4**
```
Set attributes for existing fields. Add the following attributes:

Field           Attribute
name            required
expected_price  required

After restarting the server, both fields should be not nullable.
```
## Chapter 4: Security - A Brief Introduction
**Exercise 4.1**
```
Add access rights.

Create the ir.model.access.csv file in the appropriate folder and define it in the __manifest__.py file.

Give the read, write, create and unlink permissions to the group base.group_user.
```
>Tip: the warning message in the log gives you most of the solution ;-)
## Chapter 5: Finally, Some UI To Play With
**Exercise 5.1**
```
Add an action.

Create the estate_property_views.xml file in the appropriate folder and define it in the __manifest__.py file.

Create an action for the model estate.property.
```
**Exercise 5.2**
```
Add menus.

Create the estate_menus.xml file in the appropriate folder and define it in the __manifest__.py file. Remember 
the sequential loading of the data files ;-)

Create the three levels of menus for the estate.property action created in the previous exercise. 
Refer to the Goal of this section for the expected result.
```
**Exercise 5.3**
```
Add new attributes to the fields.

Find the appropriate attributes (see Field) to:

set the selling price as read-only

prevent copying of the availability date and the selling price values
```
**Exercise 5.4**
```
Set default values.

Add the appropriate default attributes so that:

the default number of bedrooms is 2

the default availability date is in 3 months
```
>Tip: this might help you: today()

**Exercise 5.5**
```
Add active field.

Add the active field to the estate.property model.
```
**Exercise 5.6**
```
Set a default value for active field.

Set the appropriate default value for the active field so it doesn’t disappear anymore.
```
**Exercise 5.7**
```
Add state field.

Add a state field to the estate.property model. Five values are possible: New, Offer Received, Offer Accepted, 
Sold and Canceled. It must be required, should not be copied and should have its default value set to ‘New’.

Make sure to use the correct type!
```
## Chapter 6: Basic Views
**Exercise 6.1**
```
Add a custom list view.

Define a list view for the estate.property model in the appropriate XML file. Check the Goal of this 
section for the fields to display.
```
>Tips: do not add the editable="bottom" attribute that you can find in the example above. We’ll come back to it later.
 some field labels may need to be adapted to match the reference.

**Exercise 6.2**
```
Add a custom form view.

Define a form view for the estate.property model in the appropriate XML file. Check the Goal of this section 
for the expected final design of the page.
```
**Exercise 6.3**
```
Add a custom search view.

Define a search view for the estate.property model in the appropriate XML file. Check the first image of this section’s 
Goal for the list of fields.
```
**Exercise 6.4**
```
Add filter and Group By.

The following should be added to the previously created search view:

a filter which displays available properties, i.e. the state should be ‘New’ or ‘Offer Received’.

the ability to group results by postcode.
```
## Chapter 7: Relations Between Models
**Exercise 7.1**
```
Add the Real Estate Property Type table.

Create the estate.property.type model and add the following field:

Field       Type        Attributes
name        Char        required

Add the menus as displayed in this section’s Goal

Add the field property_type_id into your estate.property model and its form, tree and search views

This exercise is a good recap of the previous chapters: you need to create a model, set the model, add an action 
and a menu, and create a view.
```
>Tip: do not forget to import any new Python files in __init__.py, add new data files in __manifest.py__ or 
 add the access rights ;-)

**Exercise 7.2**
```
Add the buyer and the salesperson.

Add a buyer and a salesperson to the estate.property model using the two common models mentioned above. They should be 
added in a new tab of the form view, as depicted in this section’s Goal.

The default value for the salesperson must be the current user. The buyer should not be copied.
```
> Tip: to get the default value, check the note below or look at an 
> example [`here`](https://github.com/odoo/odoo/blob/5bb8b927524d062be32f92eb326ef64091301de1/addons/crm/models/crm_lead.py#L92).

**Exercise 7.3**
```
Add the Real Estate Property Tag table.

Create the estate.property.tag model and add the following field:

Field       Type        Attributes
name        Char        required

Add the menus as displayed in this section’s Goal

Add the field tag_ids to your estate.property model and in its form and tree views
```
>Tip: in the view, use the widget="many2many_tags" attribute as demonstrated here. 
> The widget attribute will be explained in detail in a later chapter of the training. 
> For now, you can try to adding and removing it and see the result ;-)

**Exercise 7.4**
```
Add the Real Estate Property Offer table.

Create the estate.property.offer model and add the following fields:

Field               Type                        Attributes          Values
price               Float                       no copy
status              Selection                                       Accepted, Refused
partner_id          Many2one (res.partner)      required
property_id         Many2one (estate.property)  required

Create a tree view and a form view with the price, partner_id and status fields. No need to create an action or a menu.

Add the field offer_ids to your estate.property model and in its form view as depicted in this section’s Goal.
```
## Chapter 8: Computed Fields And Onchanges
**Exercise 8.1**
```
Compute the total area.

Add the total_area field to estate.property. It is defined as the sum of the living_area and the garden_area.

Add the field in the form view as depicted on the first image of this section’s Goal.
```
**Exercise 8.2**
```
Compute the best offer.

Add the best_price field to estate.property. It is defined as the highest (i.e. maximum) of the offers’ price.

Add the field to the form view as depicted in the first image of this section’s Goal.

```
>Tip: you might want to try using the mapped() method. See [`here`](https://github.com/odoo/odoo/blob/f011c9aacf3a3010c436d4e4f408cd9ae265de1b/addons/account/models/account_payment.py#L686) 
> for a simple example.

**Exercise 8.3**
```
Compute a validity date for offers.

Add the following fields to the estate.property.offer model:

Field           Type        Default
validity        Integer     7
date_deadline   Date

Where date_deadline is a computed field which is defined as the sum of two fields from the offer: 
the create_date and the validity. Define an appropriate inverse function so that the user can set either 
the date or the validity.
```
>Tip: the create_date is only filled in when the record is created, therefore you will need a fallback to prevent crashing at time of creation.
>Add the fields in the form view and the list view as depicted on the second image of this section’s Goal.

**Exercise 8.4**
```
Set values for garden area and orientation.
Create an onchange in the estate.property model in order to set values for the garden area (10) 
and orientation (North) when garden is set to True. When unset, clear the fields.
```
## Chapter 9: Ready For Some Action?
**Exercise 9.1**
```
Cancel and set a property as sold.

Add the buttons ‘Cancel’ and ‘Sold’ to the estate.property model. A canceled property cannot be set as sold, 
and a sold property cannot be canceled.

Refer to the first image of the Goal for the expected result.
```
>Tip: in order to raise an error, you can use the UserError function. There are plenty of examples in the Odoo source code ;-)
>Add the buttons ‘Accept’ and ‘Refuse’ to the estate.property.offer model.
>Refer to the second image of the Goal for the expected result.

>Tip: to use an icon as a button, have a look at this example.
>When an offer is accepted, set the buyer and the selling price for the corresponding property.
>Refer to the third image of the Goal for the expected result.
>Pay attention: in real life only one offer can be accepted for a given property!
## Chapter 10: Constraints
**Exercise 10.1**
```
Add SQL constraints.

Add the following constraints to their corresponding models:

A property expected price must be strictly positive

A property selling price must be positive

An offer price must be strictly positive

A property tag name and property type name must be unique
```
>Tip: search for the unique keyword in the Odoo codebase for examples of unique names.

**Exercise 10.2**
```
Add Python constraints.

Add a constraint so that the selling price cannot be lower than 90% of the expected price.
```
>Tip: the selling price is zero until an offer is validated. You will need to fine tune your check to take 
> this into account.
```
Ensure the constraint is triggered every time the selling price or the expected price is changed!
```
>Warning: Always use the float_compare() and float_is_zero() methods from odoo.tools.float_utils when working 
> with floats!
## Chapter 11: Add The Sprinkles
**Exercise 11.1**
```
Add an inline list view.

Add the One2many field property_ids to the estate.property.type model.

Add the field in the estate.property.type form view as depicted in the Goal of this section.
```
**Exercise 11.2**
```
Use the status bar widget.

Use the statusbar widget in order to display the state of the estate.property as depicted in the Goal of this section.
```
>Tip: a simple example can be found [`here`](https://github.com/odoo/odoo/blob/0e12fa135882cd5095dbf15fe2f64231c6a84336/addons/account/views/account_bank_statement_views.xml#L136).

**Exercise 11.3**
```
Add model ordering.

Define the following orders in their corresponding models:

Model                   Order
estate.property         Descending ID
estate.property.offer   Descending Price
estate.property.tag     Name
estate.property.type    Name
```
**Exercise 11.4**
```
Add manual ordering.

Add the following field:

Model                   Field           Type
estate.property.type    Sequence        Integer

Add the sequence to the estate.property.type list view with the correct widget.
```
>Tip: you can find an example here: [model](https://github.com/odoo/odoo/blob/892dd6860733c46caf379fd36f57219082331b66/addons/crm/models/crm_stage.py#L36) 
> and [view](https://github.com/odoo/odoo/blob/892dd6860733c46caf379fd36f57219082331b66/addons/crm/views/crm_stage_views.xml#L23).

**Exercise 11.5**
```
Add widget options.

Add the appropriate option to the property_type_id field to prevent the creation and the editing of a property type 
from the property form view. Have a look at the Many2one widget documentation for more info.

Add the following field:

Model                   Field           Type
estate.property.tag     Color           Integer

Then add the appropriate option to the tag_ids field to add a color picker on the tags. Have a look at the 
FieldMany2ManyTags widget documentation for more info.
```
**Exercise 11.6**
```
Add conditional display of buttons.

Use the invisible attribute to display the header buttons conditionally as depicted in this section’s Goal 
(notice how the ‘Sold’ and ‘Cancel’ buttons change when the state is modified).
```
>Tip: do not hesitate to search for invisible= in the Odoo XML files for some examples.

**Exercise 11.7**
```
Use invisible.

Make the garden area and orientation invisible in the estate.property form view when there is no garden.

Make the ‘Accept’ and ‘Refuse’ buttons invisible once the offer state is set.

Do not allow adding an offer when the property state is ‘Offer Accepted’, ‘Sold’ or ‘Canceled’. To do this use the readonly attribute.
```
**Exercise 11.8**
```
Make list views editable.

Make the estate.property.offer and estate.property.tag list views editable.
```
**Exercise 11.9**
```
Make a field optional.

Make the field date_availability on the estate.property list view optional and hidden by default.
```
**Exercise 11.10**
```
Add some decorations.

On the estate.property list view:

Properties with an offer received are green

Properties with an offer accepted are green and bold

Properties sold are muted

On the estate.property.offer list view:

Refused offers are red

Accepted offers are green

The state should not be visible anymore
```
>Tips:Keep in mind that all fields used in attributes must be in the view! If you want to test the color of the 
> “Offer Received” and “Offer Accepted” states, add the field in the form view and change 
> it manually (we’ll implement the business logic for this later).

**Exercise 11.11**
```
Add a default filter.

Make the ‘Available’ filter selected by default in the estate.property action.
```

**Exercise 11.12**
```
Change the living area search.

Add a filter_domain to the living area to include properties with an area equal to or greater than the given value.
```

**Exercise 11.13**
```
Add a stat button to property type.

Add the field property_type_id to estate.property.offer. We can define it as a related field 
on property_id.property_type_id and set it as stored.

Thanks to this field, an offer will be linked to a property type when it’s created. 
You can add the field to the list view of offers to make sure it works.

Add the field offer_ids to estate.property.type which is the One2many inverse of the field defined in the previous step.

Add the field offer_count to estate.property.type. It is a computed field that counts the number of offers 
for a given property type (use offer_ids to do so).

At this point, you have all the information necessary to know how many offers are linked to a property type. 
When in doubt, add offer_ids and offer_count directly to the view. The next step is to display the 
list when clicking on the stat button.

Create a stat button on estate.property.type pointing to the estate.property.offer action. This means you should 
use the type="action" attribute (go back to the end of Chapter 9: Ready For Some Action? if you need a refresher).

At this point, clicking on the stat button should display all offers. We still need to filter out the offers.

On the estate.property.offer action, add a domain that defines property_type_id as equal to the 
active_id (= the current record, here is an example)
```
## Chapter 12: Inheritance
**Exercise 12.1**
```
Add business logic to the CRUD methods.

Prevent deletion of a property if its state is not ‘New’ or ‘Canceled’
```
>Tip: create a new method with the ondelete() decorator and remember that self can be a recordset with 
>more than one record.
```
At offer creation, set the property state to ‘Offer Received’. Also raise an error if the user tries to create 
an offer with a lower amount than an existing offer.
```
>Tip: 
> - the property_id field is available in the vals, but it is an int. 
> - To instantiate an estate.property object, use self.env[model_name].browse(value) (example)

**Exercise 12.2**
```
Add a field to Users.

Add the following field to res.users:

Field           Type
property_ids    One2many inverse of the field that references the salesperson in estate.property

Add a domain to the field so it only lists the available properties.
```

**Exercise 12.3**
```
Add fields to the Users view.

Add the property_ids field to the base.view_users_form in a new notebook page.
```
>Tip: an example an inheritance of the users’ view can be found [here](https://github.com/odoo/odoo/blob/691d1f087040f1ec7066e485d19ce3662dfc6501/addons/gamification/views/res_users_views.xml#L5-L14).

## Chapter 13: Interact With Other Modules
**Exercise 13.1**
```
Create a link module.

Create the estate_account module, which depends on the estate and account modules. For now, it will be an empty shell.
```
>Tip: you already did this at the beginning of the tutorial. The process is very similar.

**Exercise 13.2**
```
Add the first step of invoice creation.

Create a estate_property.py file in the correct folder of the estate_account module.

_inherit the estate.property model.

Override the action_sold method (you might have named it differently) to return the super call.
```
>Tip: to make sure it works, add a print or a debugger breakpoint in the overridden method.

**Exercise 13.3**
```
Add the second step of invoice creation.

Create an empty account.move in the override of the action_sold method:

- the partner_id is taken from the current estate.property

- the move_type should correspond to a ‘Customer Invoice’
```
>Tips:
>- to create an object, use self.env[model_name].create(values), where values is a dict. 
>- the create method doesn’t accept recordsets as field values.

**Exercise 13.4**
```
Add the third step of invoice creation.

Add two invoice lines during the creation of the account.move. Each property sold will be invoiced 
following these conditions:

- 6% of the selling price

- an additional 100.00 from administrative fees
```
>Tip: Add the invoice_line_ids at creation following the example above. For each line, 
>we need a name, quantity and price_unit.

## Chapter 14: A Brief History Of QWeb
**Exercise 14.1**
```
Make a minimal kanban view.

Using the simple example provided, create a minimal Kanban view for the properties. The only field to display is the name.
```
>Tip: you must add kanban in the view_mode of the corresponding ir.actions.act_window.

**Exercise 14.2**
```
Improve the Kanban view.

Add the following fields to the Kanban view: expected price, best price, selling price and tags. 
Pay attention: the best price is only displayed when an offer is received, while the selling 
price is only displayed when an offer is accepted.

Refer to the Goal of the section for a visual example.
```
**Exercise 14.3**
```
Add default grouping.

Use the appropriate attribute to group the properties by type by default. You must also prevent drag and drop.

Refer to the Goal of the section for a visual example.
```
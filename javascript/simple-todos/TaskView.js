
var TaskView = function() {
    //this.model = model;
    this.addTaskEvent = new Event(this);
    this.selectTaskEvent = new Event(this);
    this.unselectTaskEvent = new Event(this);
    this.deleteTaskEvent = new Event(this);
    this.completeTaskEvent = new Event(this);

    this.init();
}

TaskView.prototype = {

    init: function() {
        this.createChildren().enable();
    },

    createChildren: function() {
        // Cache the document object
        this.$container = $(".js-container");
        this.$taskTextbox = this.$container.find(".js-task-textbox");
        this.$addTaskButton = this.$container.find('.js-add-task-button');
        this.$tasksContainer = this.$container.find('.js-tasks-container');

        return this;
    },

    enable: function() {
        this.$addTaskButton.click(this.addTaskButton.bind(this));
        this.$container.on('click', '.js-task', this.selectOrUnselect.bind(this));
        this.$container.on('click', '.js-complete-task-button', this.completeTaskButton.bind(this));
        this.$container.on('click', '.js-delete-task-button', this.deleteTaskButton.bind(this));

        return this;
    },

    rebuildList: function(tasks) {
        var html = '';
        var $tasksContainer = this.$tasksContainer;

        $tasksContainer.html('');

        var index = 0;
        for (var task in tasks) {
            if (tasks[task].taskStatus == 'completed') {
                html += '<div style="color:green;">';
            } 
            else {
                html += '<div style="color:black;">';
            }

            $tasksContainer.append(html + '<label><input type="checkbox" class="js-task" data-index="' + index + '" data-task-selected="false">' + tasks[task].taskName + '</label></div>');

            index++;
        }
    },

    addTaskButton: function() {
        this.addTaskEvent.notify({
            task: this.$taskTextbox.val()
        });
        this.clearTaskTextbox();
    },

    completeTaskButton: function() {
        this.completeTaskEvent.notify();
    },

    deleteTaskButton: function() {
        this.deleteTaskEvent.notify();
    },

    selectOrUnselect: function() {
        var taskIndex = $(event.target).attr("data-index");
        
        if ($(event.target).attr('data-task-selected') == 'false') {
            $(event.target).attr('data-task-selected', true);
            this.selectTaskEvent.notify({
                taskIndex: taskIndex
            });
        } else {
            $(event.target).attr('data-task-selected', false);
            this.unselectTaskEvent.notify({
                taskIndex: taskIndex
            });
        }
    },

    /* ------------------------------ Handlers from Event Dispatcher ------------------------------ */


    clearTaskTextbox: function () {
        this.$taskTextbox.val('');
    },

    // addTask: function (sender, args) {
    //     this.show(sender);
    // },

    // setTasksAsCompleted: function () {
    //     this.show();
    // },

    // deleteTasks: function () {
    //     this.show();
    // }

     /* ---------------------------- End Handlers from Event Dispatcher ---------------------------- */



}
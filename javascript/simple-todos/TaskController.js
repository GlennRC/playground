var TaskController = function (model, view) {
    this.model = model;
    this.view = view;

    this.init();
};

TaskController.prototype = {

    init: function () {
        this.enable();
    },

    enable: function () {
        this.view.addTaskEvent.attach(this.addTask.bind(this));
        this.view.completeTaskEvent.attach(this.completeTask.bind(this));
        this.view.deleteTaskEvent.attach(this.deleteTask.bind(this));
        this.view.selectTaskEvent.attach(this.selectTask.bind(this));
        this.view.unselectTaskEvent.attach(this.unselectTask.bind(this));

        return this;
    },


    addTask: function (sender, args) {
        this.model.addTask(args.task);
        this.updateView();
    },

    selectTask: function (sender, args) {
        this.model.setSelectedTask(args.taskIndex);
        this.updateView();
    },

    unselectTask: function (sender, args) {
        this.model.unselectTask(args.taskIndex);
        this.updateView();
    },

    completeTask: function () {
        this.model.setTasksAsCompleted();
        this.updateView();
    },

    deleteTask: function () {
        this.model.deleteTasks();   
        this.updateView();    
    },

    updateView() {
        this.view.rebuildList(this.model.getTasks());
    }

};
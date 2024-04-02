<template>
    <div class="feedback-wrapper">
        <div class="feedback-header">
            <span class="feedback-header-text">Drop a <span class="green">feedback</span> for a <span class="green">feature</span> request or saying you simply <span class="green">like</span> the project <span class="green">:)</span></span>
        </div>
        <div class="feedback-form">
            <div class="feedback-menu">
                <select class="feedback-text">
                    <option value="featurerequest" class="feedback-option">Feature Request</option>
                    <option value="other" class="feedback-option">Other</option>
                </select>
                <!--<div class="dropdown-content">
                    <option value="featurerequest" class="feedback-option">Feature Request</option>
                    <option value="other" class="feedback-option">Other</option>
                </div>-->
            </div>
            <textarea class="feedback-textarea" placeholder="So, what is your feedback? max of 512 characters"></textarea>
            <button class="grn-btn mobile-form-btn"><span>Send feedback</span></button>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.feedback-wrapper {
    display: grid;
    align-content: start;
    row-gap: 50px;
    justify-items: center;
    width: 1000px;
    .feedback-header {
        width: 1000px;
        text-align: center;
        .feedback-header-text {
            font-family: 'medium';
            font-size: 32px;
            color: #FEFEFE;
        }
    }
    .feedback-form {
        background: #191414;
        border-radius: 20px;
        display: grid;
        justify-items: center;
        align-items: start;
        row-gap: 20px;
        padding: 10px;
        .feedback-menu {
            display: flex;
            background: transparent;
            padding-left: 10px;
            padding-right: 10px;
            border: 1px solid #FEFEFE;
            border-radius: 10px;
            .feedback-text {
                background: transparent;
                width: 400px;
                height: 38px;
                outline: 0;
                color: #FEFEFE;
                font-family: 'regular';
                border: 0;
                font-size: 15px;
                align-items: center;
                .feedback-option {
                    color:#191414;
                }
            }
        }
        .feedback-menu:focus-within {
            border: 1.5px solid #04D04D;
        }
        .feedback-textarea {
            width: 400px;
            padding: 10px;
            min-height: 200px;
            color: #FEFEFE;
            background: #191414;
            border-radius: 10px;
            border: 1.5px solid #FEFEFE;
            font-family: 'regular';
            font-size: 15px;
            letter-spacing: 1px;
        }
        .feedback-textarea:focus {
            border: 1.5px solid #04D04D;
        }
    }
}

@media only screen and (max-width: 460px) {
.feedback-wrapper {
    width: 360px;
    .feedback-header {
        width: 360px;
    }
    .feedback-form {
        .feedback-menu {
            .feedback-text {
                width: 320px;
                option {
                    width: 320px;
                }
            }
        }
        .feedback-textarea {
            width: 320px;
        }
        .mobile-form-btn {
            width: 340px;
        }
    }
}
}
</style>
# Generated from CML.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CMLParser import CMLParser
else:
    from CMLParser import CMLParser

# This class defines a complete generic visitor for a parse tree produced by CMLParser.

class CMLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CMLParser#definitions.
    def visitDefinitions(self, ctx:CMLParser.DefinitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#imports.
    def visitImports(self, ctx:CMLParser.ImportsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#topLevel.
    def visitTopLevel(self, ctx:CMLParser.TopLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#contextMap.
    def visitContextMap(self, ctx:CMLParser.ContextMapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#contextMapSetting.
    def visitContextMapSetting(self, ctx:CMLParser.ContextMapSettingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#contextMapType.
    def visitContextMapType(self, ctx:CMLParser.ContextMapTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#contextMapState.
    def visitContextMapState(self, ctx:CMLParser.ContextMapStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#relationship.
    def visitRelationship(self, ctx:CMLParser.RelationshipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#relationshipConnection.
    def visitRelationshipConnection(self, ctx:CMLParser.RelationshipConnectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#relationshipEndpoint.
    def visitRelationshipEndpoint(self, ctx:CMLParser.RelationshipEndpointContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#relationshipEndpointRight.
    def visitRelationshipEndpointRight(self, ctx:CMLParser.RelationshipEndpointRightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#relationshipKeyword.
    def visitRelationshipKeyword(self, ctx:CMLParser.RelationshipKeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#relationshipRoles.
    def visitRelationshipRoles(self, ctx:CMLParser.RelationshipRolesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#relationshipRole.
    def visitRelationshipRole(self, ctx:CMLParser.RelationshipRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#relationshipArrow.
    def visitRelationshipArrow(self, ctx:CMLParser.RelationshipArrowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#relationshipAttribute.
    def visitRelationshipAttribute(self, ctx:CMLParser.RelationshipAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#downstreamRights.
    def visitDownstreamRights(self, ctx:CMLParser.DownstreamRightsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#boundedContext.
    def visitBoundedContext(self, ctx:CMLParser.BoundedContextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#boundedContextLinkClause.
    def visitBoundedContextLinkClause(self, ctx:CMLParser.BoundedContextLinkClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#boundedContextAttribute.
    def visitBoundedContextAttribute(self, ctx:CMLParser.BoundedContextAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#boundedContextType.
    def visitBoundedContextType(self, ctx:CMLParser.BoundedContextTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#knowledgeLevel.
    def visitKnowledgeLevel(self, ctx:CMLParser.KnowledgeLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#evolutionType.
    def visitEvolutionType(self, ctx:CMLParser.EvolutionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#domain.
    def visitDomain(self, ctx:CMLParser.DomainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#subdomain.
    def visitSubdomain(self, ctx:CMLParser.SubdomainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#subdomainType.
    def visitSubdomainType(self, ctx:CMLParser.SubdomainTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#module.
    def visitModule(self, ctx:CMLParser.ModuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#tacticDDDApplication.
    def visitTacticDDDApplication(self, ctx:CMLParser.TacticDDDApplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#tacticDDDElement.
    def visitTacticDDDElement(self, ctx:CMLParser.TacticDDDElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#aggregate.
    def visitAggregate(self, ctx:CMLParser.AggregateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#domainObject.
    def visitDomainObject(self, ctx:CMLParser.DomainObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#simpleDomainObjectOrEnum.
    def visitSimpleDomainObjectOrEnum(self, ctx:CMLParser.SimpleDomainObjectOrEnumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#simpleDomainObject.
    def visitSimpleDomainObject(self, ctx:CMLParser.SimpleDomainObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#entity.
    def visitEntity(self, ctx:CMLParser.EntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#entityBody.
    def visitEntityBody(self, ctx:CMLParser.EntityBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#entityFlag.
    def visitEntityFlag(self, ctx:CMLParser.EntityFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#valueObject.
    def visitValueObject(self, ctx:CMLParser.ValueObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#valueObjectBody.
    def visitValueObjectBody(self, ctx:CMLParser.ValueObjectBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#valueObjectFlag.
    def visitValueObjectFlag(self, ctx:CMLParser.ValueObjectFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#domainEvent.
    def visitDomainEvent(self, ctx:CMLParser.DomainEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#domainEventBody.
    def visitDomainEventBody(self, ctx:CMLParser.DomainEventBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#domainEventFlag.
    def visitDomainEventFlag(self, ctx:CMLParser.DomainEventFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#commandEvent.
    def visitCommandEvent(self, ctx:CMLParser.CommandEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#commandEventBody.
    def visitCommandEventBody(self, ctx:CMLParser.CommandEventBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#commandEventFlag.
    def visitCommandEventFlag(self, ctx:CMLParser.CommandEventFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#trait.
    def visitTrait(self, ctx:CMLParser.TraitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#traitBody.
    def visitTraitBody(self, ctx:CMLParser.TraitBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#traitFlag.
    def visitTraitFlag(self, ctx:CMLParser.TraitFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#traitRef.
    def visitTraitRef(self, ctx:CMLParser.TraitRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#dataTransferObject.
    def visitDataTransferObject(self, ctx:CMLParser.DataTransferObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#dtoBody.
    def visitDtoBody(self, ctx:CMLParser.DtoBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#dtoFlag.
    def visitDtoFlag(self, ctx:CMLParser.DtoFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#dtoModifier.
    def visitDtoModifier(self, ctx:CMLParser.DtoModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#enumDecl.
    def visitEnumDecl(self, ctx:CMLParser.EnumDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#enumOption.
    def visitEnumOption(self, ctx:CMLParser.EnumOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#enumAttribute.
    def visitEnumAttribute(self, ctx:CMLParser.EnumAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#enumValue.
    def visitEnumValue(self, ctx:CMLParser.EnumValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#enumParameter.
    def visitEnumParameter(self, ctx:CMLParser.EnumParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#basicType.
    def visitBasicType(self, ctx:CMLParser.BasicTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#basicTypeBody.
    def visitBasicTypeBody(self, ctx:CMLParser.BasicTypeBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#basicTypeFlag.
    def visitBasicTypeFlag(self, ctx:CMLParser.BasicTypeFlagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#feature.
    def visitFeature(self, ctx:CMLParser.FeatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#association.
    def visitAssociation(self, ctx:CMLParser.AssociationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#attribute.
    def visitAttribute(self, ctx:CMLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#attributeAssociationLabel.
    def visitAttributeAssociationLabel(self, ctx:CMLParser.AttributeAssociationLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#attributeOption.
    def visitAttributeOption(self, ctx:CMLParser.AttributeOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#notPrefix.
    def visitNotPrefix(self, ctx:CMLParser.NotPrefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#attributeOptionKey.
    def visitAttributeOptionKey(self, ctx:CMLParser.AttributeOptionKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#oppositeHolder.
    def visitOppositeHolder(self, ctx:CMLParser.OppositeHolderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#operation.
    def visitOperation(self, ctx:CMLParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#callableOperationNoParens.
    def visitCallableOperationNoParens(self, ctx:CMLParser.CallableOperationNoParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#operationWithParams.
    def visitOperationWithParams(self, ctx:CMLParser.OperationWithParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#operationNoParams.
    def visitOperationNoParams(self, ctx:CMLParser.OperationNoParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#operationPrefix.
    def visitOperationPrefix(self, ctx:CMLParser.OperationPrefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#operationHint.
    def visitOperationHint(self, ctx:CMLParser.OperationHintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#operationHintType.
    def visitOperationHintType(self, ctx:CMLParser.OperationHintTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#operationClause.
    def visitOperationClause(self, ctx:CMLParser.OperationClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#throwsClause.
    def visitThrowsClause(self, ctx:CMLParser.ThrowsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#operationOption.
    def visitOperationOption(self, ctx:CMLParser.OperationOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#httpMethod.
    def visitHttpMethod(self, ctx:CMLParser.HttpMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#operationTail.
    def visitOperationTail(self, ctx:CMLParser.OperationTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#eventTypeRef.
    def visitEventTypeRef(self, ctx:CMLParser.EventTypeRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#operationTarget.
    def visitOperationTarget(self, ctx:CMLParser.OperationTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#contentBlock.
    def visitContentBlock(self, ctx:CMLParser.ContentBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#contentEntry.
    def visitContentEntry(self, ctx:CMLParser.ContentEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#subdomainAttribute.
    def visitSubdomainAttribute(self, ctx:CMLParser.SubdomainAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#contentItem.
    def visitContentItem(self, ctx:CMLParser.ContentItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#ownerDecl.
    def visitOwnerDecl(self, ctx:CMLParser.OwnerDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#aggregateAttribute.
    def visitAggregateAttribute(self, ctx:CMLParser.AggregateAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#volatility.
    def visitVolatility(self, ctx:CMLParser.VolatilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#criticality.
    def visitCriticality(self, ctx:CMLParser.CriticalityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#similarity.
    def visitSimilarity(self, ctx:CMLParser.SimilarityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#setting.
    def visitSetting(self, ctx:CMLParser.SettingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#moduleAttribute.
    def visitModuleAttribute(self, ctx:CMLParser.ModuleAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#parameter.
    def visitParameter(self, ctx:CMLParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#parameterList.
    def visitParameterList(self, ctx:CMLParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#type.
    def visitType(self, ctx:CMLParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#collectionType.
    def visitCollectionType(self, ctx:CMLParser.CollectionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#service.
    def visitService(self, ctx:CMLParser.ServiceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#serviceBody.
    def visitServiceBody(self, ctx:CMLParser.ServiceBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#serviceBodyElement.
    def visitServiceBodyElement(self, ctx:CMLParser.ServiceBodyElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#resource.
    def visitResource(self, ctx:CMLParser.ResourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#resourceBody.
    def visitResourceBody(self, ctx:CMLParser.ResourceBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#resourceBodyElement.
    def visitResourceBodyElement(self, ctx:CMLParser.ResourceBodyElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#consumer.
    def visitConsumer(self, ctx:CMLParser.ConsumerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#consumerBody.
    def visitConsumerBody(self, ctx:CMLParser.ConsumerBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#consumerBodyElement.
    def visitConsumerBodyElement(self, ctx:CMLParser.ConsumerBodyElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#repository.
    def visitRepository(self, ctx:CMLParser.RepositoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#repositoryBody.
    def visitRepositoryBody(self, ctx:CMLParser.RepositoryBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#repositoryBodyElement.
    def visitRepositoryBodyElement(self, ctx:CMLParser.RepositoryBodyElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#repositoryMethod.
    def visitRepositoryMethod(self, ctx:CMLParser.RepositoryMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#serviceModifier.
    def visitServiceModifier(self, ctx:CMLParser.ServiceModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#resourceModifier.
    def visitResourceModifier(self, ctx:CMLParser.ResourceModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#consumerModifier.
    def visitConsumerModifier(self, ctx:CMLParser.ConsumerModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#dependency.
    def visitDependency(self, ctx:CMLParser.DependencyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#repositoryModifier.
    def visitRepositoryModifier(self, ctx:CMLParser.RepositoryModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#repositoryMethodOption.
    def visitRepositoryMethodOption(self, ctx:CMLParser.RepositoryMethodOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#visibility.
    def visitVisibility(self, ctx:CMLParser.VisibilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#application.
    def visitApplication(self, ctx:CMLParser.ApplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#applicationElement.
    def visitApplicationElement(self, ctx:CMLParser.ApplicationElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#commandDecl.
    def visitCommandDecl(self, ctx:CMLParser.CommandDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#flow.
    def visitFlow(self, ctx:CMLParser.FlowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#flowStep.
    def visitFlowStep(self, ctx:CMLParser.FlowStepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#flowCommandStep.
    def visitFlowCommandStep(self, ctx:CMLParser.FlowCommandStepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#flowCommandTail.
    def visitFlowCommandTail(self, ctx:CMLParser.FlowCommandTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#flowEventStep.
    def visitFlowEventStep(self, ctx:CMLParser.FlowEventStepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#flowEventTriggerList.
    def visitFlowEventTriggerList(self, ctx:CMLParser.FlowEventTriggerListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#flowOperationStep.
    def visitFlowOperationStep(self, ctx:CMLParser.FlowOperationStepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#flowOperationTail.
    def visitFlowOperationTail(self, ctx:CMLParser.FlowOperationTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#flowInitiator.
    def visitFlowInitiator(self, ctx:CMLParser.FlowInitiatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#flowDelegate.
    def visitFlowDelegate(self, ctx:CMLParser.FlowDelegateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#flowInvocationList.
    def visitFlowInvocationList(self, ctx:CMLParser.FlowInvocationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#flowInvocationConnector.
    def visitFlowInvocationConnector(self, ctx:CMLParser.FlowInvocationConnectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#flowInvocation.
    def visitFlowInvocation(self, ctx:CMLParser.FlowInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#flowInvocationKind.
    def visitFlowInvocationKind(self, ctx:CMLParser.FlowInvocationKindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#flowEmitsClause.
    def visitFlowEmitsClause(self, ctx:CMLParser.FlowEmitsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#flowEventList.
    def visitFlowEventList(self, ctx:CMLParser.FlowEventListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#coordination.
    def visitCoordination(self, ctx:CMLParser.CoordinationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#coordinationStep.
    def visitCoordinationStep(self, ctx:CMLParser.CoordinationStepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#coordinationPath.
    def visitCoordinationPath(self, ctx:CMLParser.CoordinationPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#stateTransition.
    def visitStateTransition(self, ctx:CMLParser.StateTransitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#targetState.
    def visitTargetState(self, ctx:CMLParser.TargetStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#transitionOperator.
    def visitTransitionOperator(self, ctx:CMLParser.TransitionOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#useCase.
    def visitUseCase(self, ctx:CMLParser.UseCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#useCaseBody.
    def visitUseCaseBody(self, ctx:CMLParser.UseCaseBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#useCaseActor.
    def visitUseCaseActor(self, ctx:CMLParser.UseCaseActorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#useCaseSecondaryActors.
    def visitUseCaseSecondaryActors(self, ctx:CMLParser.UseCaseSecondaryActorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#useCaseInteractionsBlock.
    def visitUseCaseInteractionsBlock(self, ctx:CMLParser.UseCaseInteractionsBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#useCaseInteractionItem.
    def visitUseCaseInteractionItem(self, ctx:CMLParser.UseCaseInteractionItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#useCaseInteractionId.
    def visitUseCaseInteractionId(self, ctx:CMLParser.UseCaseInteractionIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#useCaseReadOperation.
    def visitUseCaseReadOperation(self, ctx:CMLParser.UseCaseReadOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#urFeature.
    def visitUrFeature(self, ctx:CMLParser.UrFeatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#urStoryFeature.
    def visitUrStoryFeature(self, ctx:CMLParser.UrStoryFeatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#urNormalFeature.
    def visitUrNormalFeature(self, ctx:CMLParser.UrNormalFeatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#urVerb.
    def visitUrVerb(self, ctx:CMLParser.UrVerbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#urEntityTail.
    def visitUrEntityTail(self, ctx:CMLParser.UrEntityTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#urEntityArticle.
    def visitUrEntityArticle(self, ctx:CMLParser.UrEntityArticleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#urEntityAttributes.
    def visitUrEntityAttributes(self, ctx:CMLParser.UrEntityAttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#urContainerEntity.
    def visitUrContainerEntity(self, ctx:CMLParser.UrContainerEntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#useCaseFreeText.
    def visitUseCaseFreeText(self, ctx:CMLParser.UseCaseFreeTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#userStory.
    def visitUserStory(self, ctx:CMLParser.UserStoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#userStoryBody.
    def visitUserStoryBody(self, ctx:CMLParser.UserStoryBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#userStoryXtextBody.
    def visitUserStoryXtextBody(self, ctx:CMLParser.UserStoryXtextBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#storyValuation.
    def visitStoryValuation(self, ctx:CMLParser.StoryValuationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#userStoryLine.
    def visitUserStoryLine(self, ctx:CMLParser.UserStoryLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#name.
    def visitName(self, ctx:CMLParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#useCaseBenefit.
    def visitUseCaseBenefit(self, ctx:CMLParser.UseCaseBenefitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#useCaseScope.
    def visitUseCaseScope(self, ctx:CMLParser.UseCaseScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#useCaseLevel.
    def visitUseCaseLevel(self, ctx:CMLParser.UseCaseLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#stakeholderSection.
    def visitStakeholderSection(self, ctx:CMLParser.StakeholderSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#stakeholderItem.
    def visitStakeholderItem(self, ctx:CMLParser.StakeholderItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#stakeholderGroup.
    def visitStakeholderGroup(self, ctx:CMLParser.StakeholderGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#stakeholder.
    def visitStakeholder(self, ctx:CMLParser.StakeholderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#stakeholderAttribute.
    def visitStakeholderAttribute(self, ctx:CMLParser.StakeholderAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#consequences.
    def visitConsequences(self, ctx:CMLParser.ConsequencesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#consequenceItem.
    def visitConsequenceItem(self, ctx:CMLParser.ConsequenceItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#valueRegister.
    def visitValueRegister(self, ctx:CMLParser.ValueRegisterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#valueCluster.
    def visitValueCluster(self, ctx:CMLParser.ValueClusterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#valueClusterAttribute.
    def visitValueClusterAttribute(self, ctx:CMLParser.ValueClusterAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#value.
    def visitValue(self, ctx:CMLParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#valueAttribute.
    def visitValueAttribute(self, ctx:CMLParser.ValueAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#valueElicitation.
    def visitValueElicitation(self, ctx:CMLParser.ValueElicitationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#valueElicitationOption.
    def visitValueElicitationOption(self, ctx:CMLParser.ValueElicitationOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#valueConsequenceEntry.
    def visitValueConsequenceEntry(self, ctx:CMLParser.ValueConsequenceEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#valueConsequence.
    def visitValueConsequence(self, ctx:CMLParser.ValueConsequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#valueAction.
    def visitValueAction(self, ctx:CMLParser.ValueActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#valueEpicClause.
    def visitValueEpicClause(self, ctx:CMLParser.ValueEpicClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#valueEpic.
    def visitValueEpic(self, ctx:CMLParser.ValueEpicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#valueNarrative.
    def visitValueNarrative(self, ctx:CMLParser.ValueNarrativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#valueWeigthing.
    def visitValueWeigthing(self, ctx:CMLParser.ValueWeigthingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#rawStatement.
    def visitRawStatement(self, ctx:CMLParser.RawStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#serviceCutterElement.
    def visitServiceCutterElement(self, ctx:CMLParser.ServiceCutterElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#scAggregate.
    def visitScAggregate(self, ctx:CMLParser.ScAggregateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#scEntity.
    def visitScEntity(self, ctx:CMLParser.ScEntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#scSecurityAccessGroup.
    def visitScSecurityAccessGroup(self, ctx:CMLParser.ScSecurityAccessGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#scSeparatedSecurityZone.
    def visitScSeparatedSecurityZone(self, ctx:CMLParser.ScSeparatedSecurityZoneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#scSharedOwnerGroup.
    def visitScSharedOwnerGroup(self, ctx:CMLParser.ScSharedOwnerGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#scPredefinedService.
    def visitScPredefinedService(self, ctx:CMLParser.ScPredefinedServiceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#scCompatibilities.
    def visitScCompatibilities(self, ctx:CMLParser.ScCompatibilitiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#scUseCase.
    def visitScUseCase(self, ctx:CMLParser.ScUseCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#scUseCaseElement.
    def visitScUseCaseElement(self, ctx:CMLParser.ScUseCaseElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#scIsLatencyCritical.
    def visitScIsLatencyCritical(self, ctx:CMLParser.ScIsLatencyCriticalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#scReads.
    def visitScReads(self, ctx:CMLParser.ScReadsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#scWrites.
    def visitScWrites(self, ctx:CMLParser.ScWritesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#scUseCaseNanoentities.
    def visitScUseCaseNanoentities(self, ctx:CMLParser.ScUseCaseNanoentitiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#scCharacteristic.
    def visitScCharacteristic(self, ctx:CMLParser.ScCharacteristicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#scAvailabilityCriticality.
    def visitScAvailabilityCriticality(self, ctx:CMLParser.ScAvailabilityCriticalityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#scConsistencyCriticality.
    def visitScConsistencyCriticality(self, ctx:CMLParser.ScConsistencyCriticalityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#scContentVolatility.
    def visitScContentVolatility(self, ctx:CMLParser.ScContentVolatilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#scSecurityCriticality.
    def visitScSecurityCriticality(self, ctx:CMLParser.ScSecurityCriticalityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#scStorageSimilarity.
    def visitScStorageSimilarity(self, ctx:CMLParser.ScStorageSimilarityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#scStructuralVolatility.
    def visitScStructuralVolatility(self, ctx:CMLParser.ScStructuralVolatilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#scNanoentities.
    def visitScNanoentities(self, ctx:CMLParser.ScNanoentitiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#idList.
    def visitIdList(self, ctx:CMLParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#qualifiedNameList.
    def visitQualifiedNameList(self, ctx:CMLParser.QualifiedNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#qualifiedName.
    def visitQualifiedName(self, ctx:CMLParser.QualifiedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CMLParser#channelIdentifier.
    def visitChannelIdentifier(self, ctx:CMLParser.ChannelIdentifierContext):
        return self.visitChildren(ctx)



del CMLParser
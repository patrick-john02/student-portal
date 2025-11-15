<script lang="ts">
export const description = "Announcements management page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref } from "vue"

import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbList,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"

import { Separator } from "@/components/ui/separator"

import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Input } from "@/components/ui/input"

import {
  Table,
  TableHeader,
  TableRow,
  TableHead,
  TableBody,
  TableCell,
} from "@/components/ui/table"

import {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuItem,
} from "@/components/ui/dropdown-menu"

import {
  Plus,
  MoreHorizontal,
  Megaphone,
  Calendar,
  User,
} from "lucide-vue-next"

const userRole = "Admin"

// Dummy announcement data
const announcements = ref([
  {
    id: 1,
    title: "Start of Classes for SY 2024–2025",
    category: "Academic",
    date: "2024-01-10",
    author: "Administrator",
    status: "Published",
    color: "bg-blue-500",
  },
  {
    id: 2,
    title: "Fire Safety Drill Scheduled",
    category: "General",
    date: "2024-01-08",
    author: "Office of Student Affairs",
    status: "Published",
    color: "bg-green-500",
  },
  {
    id: 3,
    title: "System Maintenance on January 15",
    category: "System",
    date: "2024-01-07",
    author: "ICT Department",
    status: "Pending",
    color: "bg-yellow-500",
  },
  {
    id: 4,
    title: "Urgent: Suspension of Classes",
    category: "Urgent",
    date: "2024-01-05",
    author: "Admin Office",
    status: "Published",
    color: "bg-red-500",
  },
])

const search = ref("")
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header class="flex h-16 shrink-0 items-center gap-2 px-4 transition-all">
        <SidebarTrigger class="-ml-2" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/admin/dashboard">Admin</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Announcements</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">

        <!-- Top Bar -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">Announcements</h2>
            <p class="text-sm text-muted-foreground">
              Manage school announcements and publication status.
            </p>
          </div>

          <Button class="flex items-center gap-2">
            <Plus class="h-4 w-4" />
            Add Announcement
          </Button>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Announcements Overview</CardTitle>
            <CardDescription>
              View, add, edit, or publish announcements.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <!-- Search -->
            <div class="flex items-center justify-between mb-4">
              <Input
                v-model="search"
                placeholder="Search announcements..."
                class="max-w-xs"
              />
            </div>

            <!-- Table -->
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-72">Title</TableHead>
                  <TableHead>Category</TableHead>
                  <TableHead>Date</TableHead>
                  <TableHead>Author</TableHead>
                  <TableHead>Status</TableHead>
                  <TableHead class="text-right w-20">Actions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="ann in announcements"
                  :key="ann.id"
                  class="hover:bg-muted/50"
                >
                  <!-- Title -->
                  <TableCell>
                    <div class="flex items-center gap-2">
                      <Megaphone class="h-4 w-4 text-muted-foreground" />
                      <span class="font-medium">{{ ann.title }}</span>
                    </div>
                  </TableCell>

                  <!-- Category -->
                  <TableCell>
                    <Badge :class="ann.color">
                      {{ ann.category }}
                    </Badge>
                  </TableCell>

                  <!-- Date -->
                  <TableCell>
                    <div class="flex items-center gap-1">
                      <Calendar class="h-3 w-3 text-muted-foreground" />
                      <span>{{ ann.date }}</span>
                    </div>
                  </TableCell>

                  <!-- Author -->
                  <TableCell>
                    <div class="flex items-center gap-1">
                      <User class="h-3 w-3 text-muted-foreground" />
                      <span>{{ ann.author }}</span>
                    </div>
                  </TableCell>

                  <!-- Status -->
                  <TableCell>
                    <Badge
                      :variant="
                        ann.status === 'Published'
                          ? 'default'
                          : 'secondary'
                      "
                    >
                      {{ ann.status }}
                    </Badge>
                  </TableCell>

                  <!-- Actions -->
                  <TableCell class="text-right">
                    <DropdownMenu>
                      <DropdownMenuTrigger as-child>
                        <Button variant="ghost" size="icon">
                          <MoreHorizontal class="h-4 w-4" />
                        </Button>
                      </DropdownMenuTrigger>

                      <DropdownMenuContent align="end">
                        <DropdownMenuLabel>Actions</DropdownMenuLabel>
                        <DropdownMenuSeparator />

                        <DropdownMenuItem>Edit Announcement</DropdownMenuItem>
                        <DropdownMenuItem>Publish</DropdownMenuItem>
                        <DropdownMenuItem>Unpublish</DropdownMenuItem>

                        <DropdownMenuSeparator />

                        <DropdownMenuItem class="text-red-600">
                          Delete Announcement
                        </DropdownMenuItem>
                      </DropdownMenuContent>
                    </DropdownMenu>
                  </TableCell>
                </TableRow>
              </TableBody>
            </Table>

          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
